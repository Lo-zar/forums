class Member:
    def __init__(self, name, age):
        self.member_id = id
        self.name = name
        self.age = age
        self.member_posts = []

    def __str__(self):
        return f"Id: {self.member_id}, name: {self.name}, age: {self.age}"


class Post:
    def __init__(self, title, body):
        self.post_id = id
        self.title = title
        self.body = body

    def __str__(self):
        return f"Id: {self.post_id}, title: {self.title}, body: {self.body}"
