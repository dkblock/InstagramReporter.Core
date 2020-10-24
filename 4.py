from datetime import datetime
import sys

from helper_methods import sign_in

if __name__ == '__main__':
    api = sign_in()
    if not api:
        sys.exit('Authentification error!')
    print('Success!\n')
    count = 5
    user_ids = [2268641338, 42415631327]
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
        records = []
        geotags = []
        for post in posts:
            description = post.get('text', '')
            location = post.get('location', {})
            if location:
                geotags.append(location.get('name',  None))
            record = {
                'id': post['pk'],
                'date': datetime.fromtimestamp(
                    post['taken_at'],
                ).strftime('%d-%m-%Y, %H:%M'),
                'description': description,
                'geotag': location.get('name',  None),
            }
            records.append(record)
        user[user_id] = {
            'geotags': geotags,
            'records': records,
        }
        users.append(user)
    print(users)
