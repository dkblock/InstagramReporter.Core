from datetime import datetime

import numpy as np

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
                'max': 'does not exist',
                'min': 'does not exist',
                'middle': 'does not exist',
                'records': [],
            }
            users.append(user)
            continue
        records = []
        likes_counts = []
        for post in posts:
            description = post.get('text', '')
            likes_counts.append(post['like_count'])
            record = {
                'id': post['pk'],
                'date': datetime.fromtimestamp(
                    post['taken_at'],
                ).strftime('%d-%m-%Y, %H:%M'),
                'description': description,
                'count': post['like_count'],
            }
            records.append(record)
        user[user_id] = {
            'max': max(likes_counts),
            'min': min(likes_counts),
            'middle': round(np.mean(likes_counts), 2),
            'records': records,
        }
        users.append(user)
    print(users)
