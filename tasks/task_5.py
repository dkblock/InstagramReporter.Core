from datetime import datetime

import numpy as np

from helper_methods import get_user_ids


def get_records(posts):
    likes_counts = []
    records = []
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
    return likes_counts, records


def main(api):
    print('Введите количество записей, которые добавить в вывод: ', end='')
    count = int(input())
    user_ids = get_user_ids()
    users = []
    for user_id in user_ids:
        user = {}
        posts = api.get_last_feed(user_id, count)
        if not len(posts):
            user[user_id] = {
                'max': 'does not exist',
                'min': 'does not exist',
                'middle': 'does not exist',
                'records': [],
            }
            users.append(user)
            continue
        likes_counts, records = get_records(posts)
        user[user_id] = {
            'max': max(likes_counts),
            'min': min(likes_counts),
            'middle': round(np.mean(likes_counts), 2),
            'records': records,
        }
        users.append(user)
    return users
