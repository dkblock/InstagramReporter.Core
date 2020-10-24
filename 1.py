import sys

from helper_methods import sign_in


if __name__ == '__main__':
    api = sign_in()
    if not api:
        sys.exit('Authentification error!')
    print('Success!\n')
    user_ids = [42415631327]
    answer = {}
    for user_id in user_ids:
        celebritys = []
        followings = api.get_followings(user_id)
        for following in followings:
            profile_info = api.get_profile_info(following["pk"])['user']
            celebrity = {}
            if profile_info['follower_count'] > 100000:
                celebrity[profile_info['pk']] = {
                    'name': profile_info['full_name'],
                    'followers': profile_info['follower_count'],
                    'description': profile_info['biography'],
                }
                celebritys.append(celebrity)
                # print(celebrity)
        answer[user_id] = celebritys
    print(celebritys)
