import sys

from tasks.helper_methods import pretty, sign_in


def test():
    return 133


def get_celebrities(api, followings):
    celebrities = []
    for following in followings:
        profile_info = api.get_profile_info(following["pk"])['user']
        celebrity = {}
        if profile_info['follower_count'] > 100000:
            celebrity[profile_info['pk']] = {
                'name': profile_info['full_name'],
                'followers': profile_info['follower_count'],
                'description': profile_info['biography'],
            }
            celebrities.append(celebrity)
    return celebrities


def main():
    api = sign_in()
    if not api:
        sys.exit('Authentification error!')
    print('Success!\n')
    user_ids = [42415631327]
    users = {}
    for user_id in user_ids:
        followings = api.get_followings(user_id)
        users[user_id] = get_celebrities(api, followings)
    print(pretty(users))
