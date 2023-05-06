# import json
#import pymysql
#
# with open("users_test.json", "r", encoding="utf-8") as read_file:
#     users = json.load(read_file)
#     print(users)
# #for a in range(len(users)):
# for i in range(len(users)-1):
#     if (users[f"{i}"]["user_id"] == users[f"{i+1}"]["user_id"]):
#         print("Обнаружен повторный пользователь")
#         del users[f"{i+1}"]
#         print(users)
#         with open("users_test.json", "w", encoding="utf-8") as file:
#             json.dump(users, file, ensure_ascii=None)

# with open("users.json", "r", encoding="utf-8") as read_file:
#     users = json.load(read_file)
#     # users = db.keys()
# print(users)
# for a in range(len(users)):
#     if (msg.from_user.id == users[f"{a}"]["user_id"]):
#         print("Пользователь уже есть")
#         break
# else:
#     print("Новый пользователь")
#     users.update({
#         len(users): {
#             "user_id": msg.from_user.id,
#             "full_name": msg.from_user.full_name,
#             "user_name": msg.from_user.username
#         }
#     })
#     with open("users.json", "w", encoding="utf-8") as file:
#         json.dump(users, file, ensure_ascii=None)
import sqlite3

db = sqlite3.connect('DB.db')

cur = db.cursor()

cur.execute("""CREATE TABLE users (
    id INTEGER,
    user_id INTEGER,
    full_name TEXT,
    username TEXT,
    join_data TEXT    
)""")

db.close()