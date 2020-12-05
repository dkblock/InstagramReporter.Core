from instapi.instapi import InstAPI

mock_users = [
    {
        'user': {
            'pk': 1,
            'follower_count': 100000,
            'full_name': 'AAA',
            'biography': 'BBB',
        },
    },
    {
        'user': {
            'pk': 2,
            'follower_count': 100001,
            'full_name': 'AAA',
            'biography': 'BBB',
        },
    },
    {
        'user': {
            'pk': 1,
            'follower_count': 100000,
            'full_name': 'AAA',
            'biography': 'only sport',
        },
    },
]

mock_record = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'like_count': 99,
    },
]

mock_two_records = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'like_count': 99,
    },
    {
        'pk': 2,
        'taken_at': 1528797322,
        'like_count': 101,
    },
]

mock_record_with_text = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'text': '123',
    },
]

mock_record_with_tags = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'text': 'I like #sport and #travel',
        'location': {
            'name': 'Yaroslavl',
        },
    },
]

mock_records_with_same_geotags = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'text': '1',
        'location': {
            'name': 'Yaroslavl',
        },
    },
    {
        'pk': 2,
        'taken_at': 1528797322,
        'text': '2',
        'location': {
            'name': 'Yaroslavl',
        },
    },
]

mock_records_with_different_geotags = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'text': '1',
        'location': {
            'name': 'Yaroslavl',
        },
    },
    {
        'pk': 2,
        'taken_at': 1528797322,
        'text': '2',
        'location': {
            'name': 'Moscow',
        },
    },
]

mock_three_records = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'like_count': 2,
    },
    {
        'pk': 2,
        'taken_at': 1528797322,
        'like_count': 4,
    },
    {
        'pk': 3,
        'taken_at': 1528797322,
        'like_count': 4,
    },
]

mock_record_without_likes = [
    {
        'pk': 1,
        'taken_at': 1528797322,
        'like_count': 0,
    },
]

api = InstAPI('', '')
