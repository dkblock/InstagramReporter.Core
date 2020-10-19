from instapi.instapi import InstAPI


if __name__ == '__main__':
    username = 'subd_sequrity'
    password = 'Subd123'
    insta = InstAPI(username, password)
    if insta.login():
        print('Login success!\n')
    user_ids = [42415631327]
    answer = {}
    for user_id in user_ids:
        celebritys = []
        followings = insta.get_followings(user_id)
        for following in followings:
            profile_info = insta.get_profile_info(following["pk"])
            celebrity = {}
            if profile_info['user']['follower_count'] > 100000:
                celebrity[profile_info['user']['pk']] = {
                    'name': profile_info['user']['full_name'],
                    'followers': profile_info['user']['follower_count'],
                    'description': profile_info['user']['biography'],
                }
                celebritys.append(celebrity)
                print(celebrity)
        answer[user_id] = celebritys
    print(celebritys)
