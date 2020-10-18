from instapi.instapi import InstAPI

if __name__ == '__main__':
    usr = "subd_sequrity"
    pasw = "Subd123"
    parser = InstAPI(usr, pasw)
    if parser.login():
        print('Login success!\n')
    answer = parser.get_id_by_username('iurii_kazanov')
    print(answer)
