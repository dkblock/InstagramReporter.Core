import json


def find_tags(biography, tags):
    finded_tags = []
    for tag in tags:
        if biography.find(tag) != -1:
            finded_tags.append(tag)
    return finded_tags


def get_blogs(api, followings, tags):
    blogs = []
    for following in followings:
        profile_info = api.get_profile_info(following['pk'])['user']
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
    return blogs


def main(api, usernames):
    user_ids = api.get_ids_by_usernames(usernames)
    tags = ["travel", "sport", "cooking", "кухня", "спорт", "фитнес"]
    users = {}
    for user_id in user_ids:
        followings = api.get_followings(user_id)
        users[user_id] = get_blogs(api, followings, tags)
    return users
