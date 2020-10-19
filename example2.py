from instapi.instapi import InstAPI

if __name__ == '__main__':
    usr = "subd_sequrity"
    pasw = "Subd123"
    parser = InstAPI(usr, pasw)
    if parser.login():
        print('Login success!\n')
    answer = parser.get_profile_info(2268641338)
    print(answer)
