from datetime import datetime

from helper_methods import sign_in


def get_records(posts):
    geotags = set()
    records = []
    for post in posts:
        description = post.get('text', '')
        location = post.get('location', {})
        if location:
            geotags.add(location.get('name',  None))
        record = {
            'id': post['pk'],
            'date': datetime.fromtimestamp(
                post['taken_at'],
            ).strftime('%d-%m-%Y, %H:%M'),
            'description': description,
            'geotag': location.get('name',  None),
        }
        records.append(record)
    return list(geotags), records


def main():
    api = sign_in()
    print('Введите количество записей, которые добавить в вывод: ', end='')
    count = int(input())
    user_ids = [42415631327]
    users = []
    for user_id in user_ids:
        user = {}
        posts = api.get_last_feed(user_id, count)
        if not len(posts):
            user[user_id] = {
                'geotags': [],
                'records': [],
            }
            users.append(user)
            continue
        geotags, records = get_records(posts)
        user[user_id] = {
            'geotags': geotags,
            'records': records,
        }
        users.append(user)
    return users
