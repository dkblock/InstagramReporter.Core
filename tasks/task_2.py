import json


def find_tags(biography, tags):
    found_tags = []
    for tag in tags:
        if biography.find(tag) != -1:
            found_tags.append(tag)
    return found_tags


def get_blogs(api, followings, tags):
    blogs = []
    for following in followings:
        profile_info = api.get_profile_info(following['pk'])['user']
        blog = {}
        found_tags = find_tags(profile_info['biography'].lower(), tags)
        if found_tags:
            blog[profile_info['pk']] = {
                'name': profile_info['full_name'],
                'followers': profile_info['follower_count'],
                'description': profile_info['biography'],
                'tags': found_tags,
            }
            blogs.append(blog)
    return blogs


def main(api, user_ids):
    with open('data/tags.json', encoding='utf-8') as tags_data:
        tags = json.load(tags_data)        
    users = {}
    for user_id in user_ids:
        followings = api.get_followings(user_id)
        users[user_id] = get_blogs(api, followings, tags)
    return users
