import json
import getpass
import sys
from unittest.mock import patch

from instapi.instapi import InstAPI


def pretty(dictionary):
    return json.dumps(
        dictionary,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False,
    )


def sign_in():
    api = InstAPI()
    if not api.login():
        sys.exit('Неверный логин или пароль!')
    print('Успешно!\n')
    return api


def get_user_ids():
    print('Введите id пользователей, разделяя их пробелом: ', end='')
    return input().split(' ')


def error_handler(func):
    """Catch exceptions.

    :param func: function which use decorator
    :return: inner_function
    """
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            sys.exit("Чтобы запустить приложение используйте комманду: 'python3 main.py <номер задания>'")  # noqa: E501
        except ModuleNotFoundError:
            sys.exit('Номер задания должен быть в диапазоне от 1 до 5')
        except Exception as error:
            sys.exit(f'Произошла непредвиденная ошибка: {error}')
    return inner_function


def patch_handler(func):

    @patch.object(getpass, 'getpass')
    @patch('builtins.input', return_value='')
    @patch.object(InstAPI, 'get_last_feed')
    @patch.object(InstAPI, 'get_profile_info')
    @patch.object(InstAPI, 'get_followings')
    @patch.object(InstAPI, 'login')
    def inner_function(*args, **kwargs):
        func(*args, **kwargs)
    return inner_function
