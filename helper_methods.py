import getpass

from instapi.instapi import InstAPI


def sign_in():
    print('Введите логин: ', end='')
    username = input()
    password = getpass.getpass('Введите пароль: ')
    insta = InstAPI(username, password)
    if insta.login():
        return insta
