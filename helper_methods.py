import json
# import getpass
import sys

from instapi.instapi import InstAPI


def pretty(dictionary):
    return json.dumps(
        dictionary,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False,
    )


def sign_in():
    username = 'subd_sequrity'
    password = 'Subd123'
    api = InstAPI(username, password)
    if not api.login():
        sys.exit('Неверный логи или пароль!')
    print('Успешно!\n')
    return api
