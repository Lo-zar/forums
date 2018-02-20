class Member:
    def __init__(self, name, age):
        self.member_id = id
        self.name = name
        self.age = age
        self.member_posts = []


class Post:
    def __init__(self, title, body):
        self.post_id = id
        self.title = title
        self.body = body

    def __str__(self):
        return f"id: {self.post_id}, title: {self.title}, body: {self.body}"
    
