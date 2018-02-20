import models
import stores

Member1 = models.Member("SIZER", "25")
Member2 = models.Member("LO-ZAR", "24")

Post1 = models.Post("Test", "This text is a test of the quality of work")
Post2 = models.Post("help my", "whan you walk on a stret and...... next time ")
Post3 = models.Post("Freedom", "From the first line of the first chapter of the Green Book")

Member_store = stores.MemberStore()
Post_store = stores.PostStore()

Member_store.add(Member1)
Member_store.add(Member2)

Post_store.add(Post1)
Post_store.add(Post2)
Post_store.add(Post3)

