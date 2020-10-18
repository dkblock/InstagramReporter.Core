import hashlib
import hmac
import json
import sys
import time
import urllib
import uuid

import requests


class InstAPI:
    API_URL = 'https://i.instagram.com/api/v1/'
    DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
                       'model': 'HM 1SW',
                       'android_version': 18,
                       'android_release': '4.3'}
    USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(  # noqa: E501
        **DEVICE_SETTINTS
    )
    IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'  # noqa: E501
    SIG_KEY_VERSION = '4'

    def __init__(self, username, password):
        md5 = hashlib.md5()
        md5.update(username.encode('utf-8') + password.encode('utf-8'))
        self.device_id = self.generate_device_id(md5.hexdigest())
        self.username = username
        self.password = password
        self.uuid = str(uuid.uuid4())
        self.is_authorized = False
        self.last_response = None
        self.session = requests.Session()

    def generate_device_id(self, seed):
        salt = "12345"
        md5 = hashlib.md5()
        md5.update(seed.encode('utf-8') + salt.encode('utf-8'))
        return f'android-{md5.hexdigest()}'[:16]

    def login(self):
        if self.is_authorized:
            return
        guid = str(uuid.uuid4()).replace('-', '')
        if self.send_request(
            f'si/fetch_headers/?challenge_type=signup&guid={guid}',
            None,
            True,
        ):
            data = {'phone_id': str(uuid.uuid4()),
                    '_csrftoken': self.last_response.cookies['csrftoken'],
                    'username': self.username,
                    'guid': self.uuid,
                    'device_id': self.device_id,
                    'password': self.password,
                    'login_attempt_count': '0'}

            if self.send_request(
                'accounts/login/',
                self.generate_signature(json.dumps(data)),
                True,
            ):
                self.is_authorized = True
                self.username_id = self.last_json["logged_in_user"]["pk"]
                self.rank_token = "%s_%s" % (self.username_id, self.uuid)
                self.token = self.last_response.cookies["csrftoken"]

                return True

    def send_request(self, endpoint, post=None, login=False):
        verify = True  # don't show request warning

        if not self.is_authorized and not login:
            raise ValueError("Not authorized!\n")

        self.session.headers.update(
            {
                'Connection': 'close',
                'Accept': '*/*',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',  # noqa: E501
                'Cookie2': '$Version=1',
                'Accept-Language': 'en-US',
                'User-Agent': self.USER_AGENT,
            },
        )

        try:
            if post:
                response = self.session.post(
                    self.API_URL + endpoint,
                    data=post,
                    verify=verify,
                )
            else:
                response = self.session.get(
                    self.API_URL + endpoint,
                    verify=verify,
                )
        except Exception as e:
            print('Except on SendRequest (wait 60 sec and resend): ' + str(e))
            time.sleep(60)

        if response.status_code == 200:
            self.last_response = response
            self.last_json = json.loads(response.text)
            return json.loads(response.text)
        else:
            try:
                self.last_response = response
                self.last_json = json.loads(response.text)
            except Exception as e:
                print(str(e))

    def generate_signature(self, data, skip_quote=False):
        if not skip_quote:
            try:
                parsed_data = urllib.parse.quote(data)
            except AttributeError:
                parsed_data = urllib.quote(data)
        else:
            parsed_data = data
        signed_body = hmac.new(
            self.IG_SIG_KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256,
        ).hexdigest() + '.' + parsed_data
        return f'ig_sig_key_version={self.SIG_KEY_VERSION}&signed_body={signed_body}'  # noqa: E501

    def get_profile_info(self, user_id):
        return self.send_request('users/' + str(user_id) + '/info/')

    def get_user_followings(self, user_id, maxid=''):
        url = 'friendships/' + str(user_id) + '/following/?'
        query_string = {
            'ig_sig_key_version': self.SIG_KEY_VERSION,
            'rank_token': self.rank_token,
        }
        if maxid:
            query_string['max_id'] = maxid
        if sys.version_info.major == 3:
            url += urllib.parse.urlencode(query_string)
        else:
            url += urllib.urlencode(query_string)
        return self.send_request(url)

    def get_followings(self, user_id):
        followings = []
        next_max_id = ''
        while True:
            temp = self.get_user_followings(user_id, next_max_id)

            for item in temp["users"]:
                followings.append(item)

            if not temp["big_list"]:
                return followings
            next_max_id = temp["next_max_id"]

    def get_id_by_username(self, username):
        user_info = self.send_request(
            'users/' + str(username) + '/usernameinfo/',
        )
        return user_info.get('user').get('pk')
