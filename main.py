import models
import stores

Member1 = models.Member("SIZER", "25")
Member2 = models.Member("LO-ZAR", "24")

Post1 = models.Post("Test", "This text is a test of the quality of work")
Post2 = models.Post("help my", "whan you walk on a stret and...... next time ")
Post3 = models.Post("Freedom", "From the first line of the first chapter of the Green Book")

member_store = stores.MemberStore()
member_store.add(Member1)
member_store.add(Member2)
member_store.delete(1)

Post_store = stores.PostStore()
Post_store.add(Post1)
Post_store.add(Post2)
Post_store.add(Post3)
Post_store.delete(1)

print(Post1)
print(Member1)
print(member_store.get_all())
print(member_store.get_by_id(2))
print(Post_store.get_all())
print(Post_store.get_by_id(2))
