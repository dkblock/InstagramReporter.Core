from InstagramAPI import InstagramAPI


class InstaParser(InstagramAPI):
    def __init__(self, username, password):
        super().__init__(username, password)

    def get_followers(self, user_id):
        next_max_id = ''
        followers = []
        while True:
            if self.getUserFollowers(user_id, next_max_id):
                temp = self.LastJson
                for item in temp["users"]:
                    followers.append(item)
                if not temp.get("big_list"):
                    return followers
                next_max_id = temp["next_max_id"]


if __name__ == '__main__':
    usr = "subd_sequrity"
    pasw = "Subd123"
    parser = InstaParser(usr, pasw)
    parser.login()
    args = [2268641338]
    total_results = []
    for arg in args:
        results = parser.get_followers(arg)
        print(len(results))
