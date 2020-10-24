import getpass
import json

from instapi.instapi import InstAPI


def sign_in():
    # print('Введите логин: ', end='')
    # username = input()
    # password = getpass.getpass('Введите пароль: ')
    username = 'subd_sequrity'
    password = 'Subd123'
    insta = InstAPI(username, password)
    if insta.login():
        return insta


def pretty(dictionary):
    return json.dumps(
        dictionary,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False,
    )
