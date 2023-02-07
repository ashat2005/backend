import sqlite3
db = sqlite3.connect('test.db')
c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS user(
name text,
title text,
view integer,
nick text
)
""");
# c.execute("INSERT INTO user VALUES('Samat', 'samat no', 10,'Samat')");
# c.execute("UPDATE user SET name = 'Dasha' WHERE rowid=1")
# c.execute("UPDATE user SET name = 'Dasha' WHERE rowid=2")
# c.execute("UPDATE user SET name = 'Dasha' WHERE rowid=3")
c.execute("UPDATE user SET name = 'x' WHERE rowid > 3")
c.execute("UPDATE user SET view = 11 WHERE  view >= 10")
c.execute("UPDATE user SET nick = 'proger' WHERE rowid = 3")
c.execute("DELETE FROM user WHERE rowid != 1")
c.execute("SELECT rowid,* FROM user")
item=c.fetchall()
for i in item:
    print(i)
db.commit()
db.close()
print("COM")