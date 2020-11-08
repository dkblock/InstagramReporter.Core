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
            else:
                print("Bad request")
                return


if __name__ == '__main__':
    username = "subd_sequrity"
    password = "Subd123"
    parser = InstaParser(username, password)
    parser.login()
    user_ids = [2268641338]
    total_results = []
    for user_id in user_ids:
        followers = parser.get_followers(user_id)
        if followers:
            print(len(followers))
