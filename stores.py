class MemberStore():
    Members = []

    def get_all(self):
        return self.Members

    def add(self, member):
        self.Members.append(member)


class PostStore():
    Posts = []

    def get_all(self):
        return self.Posts

    def add(self, post):
        self.Posts.append(post)
