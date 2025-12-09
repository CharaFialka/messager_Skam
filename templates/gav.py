import sqlite3
data_base= sqlite3.connect("skam.db", check_same_thread=False)
cursor = data_base.cursor()
# cursor.execute("""INSERT INTO chats(name) VALUES('котогусеницы')""")
# cursor.execute("""INSERT INTO chat_users(chat_id,user_id)
# VALUES(1,1)""")
# cursor.execute("""INSERT INTO chat_users(chat_id,user_id)
# VALUES(1,2)""")

cursor.execute("""INSERT INTO messages(content, chat_id, user_id)
VALUES('С Новым Годом!!!!!!!!!!!!!!!!!!', 1,1);
""")
cursor.execute("""INSERT INTO messages(content, chat_id, user_id)
VALUES('Весёлые тюленчики уже празднуют :3', 1,2)""")
data_base.commit()
