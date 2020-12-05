from datetime import datetime
import re

from helper_methods import get_user_ids


def get_hashtags(description):
    reg = re.compile(r'#(\w+)')
    return reg.findall(description)


def get_records(posts):
    records = []
    for post in posts:
        description = post.get('text', '')
        tags = []
        if description:
            tags = get_hashtags(description)
        record = {
            'id': post['pk'],
            'date': datetime.fromtimestamp(
                post['taken_at'],
            ).strftime('%d-%m-%Y, %H:%M'),
            'description': description,
            'tags': tags,
        }
        records.append(record)
    return records


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
                'last_activity': 'does not exist',
                'frequency': 0,
                'records': [],
            }
            users.append(user)
            continue
        last_activity_dt = datetime.fromtimestamp(posts[0]['taken_at'])
        first_activity_dt = datetime.fromtimestamp(posts[-1]['taken_at'])
        interval = (last_activity_dt - first_activity_dt).days
        frequency = round(count / interval, 2) if interval else count
        user[user_id] = {
            'last_activity': last_activity_dt.strftime('%d-%m-%Y, %H:%M'),
            'frequency': frequency,
            'records': get_records(posts),
        }
        users.append(user)
    return users
