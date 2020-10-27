# import getpass
import sys

from instapi.instapi import InstAPI


def error_handler(func):
    '''Декоратор для обработки исключений.'''
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


def sign_in(func):
    '''Декоратор для авторизации.'''
    def inner_function(*args, **kwargs):
        # print('Введите логин: ', end='')
        # username = input()
        # password = getpass.getpass('Введите пароль: ')
        username = 'subd_sequrity'
        password = 'Subd123'
        api = InstAPI(username, password)
        if not api.login():
            sys.exit('Неверный логи или пароль!')
        print('Успешно!\n')
        func(api)
    return inner_function
