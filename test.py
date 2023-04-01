import json

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

# msg_from_user_id = 1206824363
#
# with open("users.json", "r", encoding="utf-8") as read_file:
#     users = json.load(read_file)
#     print(users)
# for a in range(len(users)):
#     if (msg_from_user_id == users[f"{a}"]["user_id"]):
#       print("Пользователь уже есть")
#       break
# else:
#     print("Новый пользователь")
#     # users["1"]["user_id"] = msg.from_user.id
#     # users["1"]["username"] = msg.from_user.full_name
#     # users.update({len(users):{("user_id", msg.from_user.id), ("username", msg.from_user.full_name)}})
#     users.update({
#       len(users): {
#         "user_id": [msg_from_user_id],
#         "username": msg.from_user.full_name
#       }
#     })
#     # user_id.append(msg.from_user.id)
#     # user_name.append(msg.from_user.full_name)
#     # users["user_id"] = user_id
#     # users["username"] = user_name
#     with open("users.json", "w", encoding="utf-8") as file:
#       json.dump(users, file, ensure_ascii=None)


import datetime

dt_now = datetime.datetime.now()
print(dt_now)