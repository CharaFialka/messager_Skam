import sqlite3

data_base= sqlite3.connect("skam.db", check_same_thread=False)
cursor = data_base.cursor()

cursor.execute("""Create TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE NOT NULL,
                                 phnonenumber VARCHAR(40) UNIQUE NOT NULL, password TEXT NOT NULL);""")

cursor.execute("CREATE TABLE IF NOT EXISTS chats(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(50));")
cursor.execute("""CREATE TABLE IF NOT EXISTS chat_users(id INTEGER PRIMARY KEY AUTOINCREMENT,chat_id INTEGER, user_id INTEGER,
                                     FOREIGN KEY (chat_id) REFERENCES chats(id),FOREIGN KEY (user_id) REFERENCES users(id), 
                                     UNIQUE(chat_id,user_id));""")
cursor.execute("""CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL,chat_id INTEGER,user_id INTEGER,
                                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN Key  (chat_id) REFERENCES chats(id),
                                   FOREIGN Key  (user_id) REFERENCES users(id));""")

data_base.commit()

def create_user(name,phnonenumber, password):
    try:
        cursor.execute(f"INSERT INTO users(name,phnonenumber,password) VALUES('{name}','{phnonenumber}', '{password}');")
        data_base.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    
def get_user_by_id(id):
    cursor.execute(f"SELECT * FROM users WHERE id = '{id}'")
    user = cursor.fetchone()
    return user

def get_user_by_name(name):
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    user = cursor.fetchone()
    return user

def get_chats(id):
    cursor.execute(f"""SELECT chats.id, name, user_id FROM chat_users INNER JOIN chats ON chat_users.chat_id= chats.id Where user_id={id};""")
    chats=cursor.fetchall()
    return chats

def get_messages(chat_id):
    cursor.execute(f"""SELECT * FROM messages WHERE chat_id={chat_id}""")
    messages = cursor.fetchall()
    return messages  