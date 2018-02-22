class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members


    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1


    def get_by_id(self, id):
        member_list = self.get_all()
        for member in member_list:
            if member.id == id:
                return member
        return None



    def entity_exists(self, member):
        result = True

        if self.get_by_id(member.id) is None:
            result = False
        return result


    def delete(self, id):
        member_list = self.get_all()
        for member in member_list:
            if member is not None:
                MemberStore.members.remove(member)



class PostStore:
    posts = []
    last_id = 1


    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1


    def get_all(self):
        return PostStore.posts


    def get_by_id(self, id):
        post_list = self.get_all()
        for post in post_list:
            if post.id == id:
                return post
        return None

    def entity_exists(self, post):
        result = True

        if self.get_by_id(post.id) is None:
            result = False
        return result


    def delete(self, id):
        post_list = self.get_all()
        for post in post_list:
            if post is not None:
                PostStore.posts.remove(post)
