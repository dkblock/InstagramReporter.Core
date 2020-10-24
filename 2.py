import sys

from helper_methods import sign_in


def find_tags(biography, tags):
    finded_tags = []
    for tag in tags:
        if biography.find(tag) != -1:
            finded_tags.append(tag)
    return finded_tags


if __name__ == '__main__':
    api = sign_in()
    if not api:
        sys.exit('Authentification error!')
    print('Success!\n')
    user_ids = [42415631327]
    tags = ['travel', 'sport', 'cooking', 'кухня', 'спорт', 'фитнес']
    answer = {}
    for user_id in user_ids:
        blogs = []
        followings = api.get_followings(user_id)
        for following in followings:
            profile_info = api.get_profile_info(following["pk"])['user']
            blog = {}
            finded_tags = find_tags(profile_info['biography'].lower(), tags)
            if finded_tags:
                blog[profile_info['pk']] = {
                    'name': profile_info['full_name'],
                    'followers': profile_info['follower_count'],
                    'description': profile_info['biography'],
                    'tags': finded_tags,
                }
                blogs.append(blog)
                # print(blog)
        answer[user_id] = blogs
    print(answer)
