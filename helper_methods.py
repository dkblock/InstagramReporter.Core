import getpass
import json
import sys
from unittest.mock import patch

from instapi.instapi import InstAPI


def print_tasks():
    print('\n1. Определить, на каких известных личностей подписан пользователь')
    print('2. Определить, на какие блоги подписан пользователь')
    print('3. Определить, насколько активно пользователь ведёт свою страницу')
    print('4. Получить геометки с последних публикаций пользователя')
    print('5. Получить максимальное/минимальное и среднее количество лайков по последним записям\n')  # noqa: E501


def check_next_task():
    print('\nПродолжить? Y/N (да/нет): ', end='')
    answer = input()
    if answer.lower() == 'n':
        sys.exit()
    elif answer.lower() != 'y':
        print('Ошибка! Введите Y/N!')
        check_next_task()


def pretty(dictionary):
    return json.dumps(
        dictionary,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False,
    )


def sign_in():
    print('Введите логин: ', end='')
    username = input()
    password = getpass.getpass('Введите пароль: ')
    api = InstAPI(username, password)
    if not api.login():
        sys.exit('Неверный логин или пароль!')
    print('Аутентификация прошла успешно!\n')
    return api


def get_user_ids(api):
    usernames = get_users()
    user_ids = []
    for username in usernames:
        user_id = api.get_id_by_username(username)
        user_ids.append(user_id)
    return user_ids


def get_users():
    print('1. Из файла (data/users.json)')
    print('2. Вручную')
    print('Выберите способ ввода пользователей: ', end='')
    answer = input()

    if answer == '1':
        return get_users_from_file()
    elif answer == '2':
        return get_users_manually()
    return get_users()


def get_users_from_file():
    with open('data/users.json') as users_data:
        users = json.load(users_data)
    return users


def get_users_manually():
    print('Введите имена пользователей, разделяя их пробелом: ', end='')
    return input().split(' ')


def error_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            sys.exit(f'Произошла непредвиденная ошибка: {error}')
    return inner_function


def patch_handler(func):
    @patch('builtins.input', return_value='')
    @patch.object(InstAPI, 'get_last_feed')
    @patch.object(InstAPI, 'get_profile_info')
    @patch.object(InstAPI, 'get_followings')
    def inner_function(*args, **kwargs):
        func(*args, **kwargs)
    return inner_function
