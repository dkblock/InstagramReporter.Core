from datetime import datetime
import re

from instapi.instapi import InstAPI

if __name__ == '__main__':
    username = 'subd_sequrity'
    password = 'Subd123'
    insta = InstAPI(username, password)
    if insta.login():
        print('Login success!\n')
    count = 5
    user_ids = [2268641338, 42415631327]
    users = []
    for user_id in user_ids:
        user = {}
        posts = insta.get_last_feed(user_id, count)
        if not len(posts):
            user[user_id] = {
                'last_activity': 'does not exist',
                'frequency': 0,
                'records': [],
            }
            users.append(user)
            continue
        last_activity_dt = datetime.fromtimestamp(posts[0]['taken_at'])
        first_activity_dt = datetime.fromtimestamp(posts[-1]['taken_at'])
        frequency = round(
            count / (last_activity_dt - first_activity_dt).days,
            2,
        )
        records = []
        for post in posts:
            description = post.get('text', '')
            if not description:
                tags = []
            else:
                words = re.split('\n| ', description)
                tags = list(filter(lambda word: word[0] == '#', words))
            record = {
                'id': post['pk'],
                'date': datetime.fromtimestamp(post['taken_at']),
                'description': description,
                'tags': tags,
            }
            records.append(record)
        user[user_id] = {
            'last_activity': last_activity_dt,
            'frequency': frequency,
            'records': records,
        }
        users.append(user)
    print(users)
