from app import db

# db.create_all()

from app import Db_Content
# try:
#     item = Db_Content(name="NoobScience", content="Hello World", time="12:48:00")
#     db.session.add(item)
#     db.session.commit()
# except:
#     pass
# db.drop_all()
x = Db_Content.query.all()
for i in x:
    print(i.name)
    print(i.content)
    print(i.time)