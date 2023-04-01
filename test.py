import json

with open("users_test.json", "r", encoding="utf-8") as read_file:
    users = json.load(read_file)
    print(users)
#for a in range(len(users)):
for i in range(len(users)-1):
    if (users[f"{i}"]["user_id"] == users[f"{i+1}"]["user_id"]):
        print("Обнаружен повторный пользователь")
        del users[f"{i+1}"]
        print(users)
        with open("users_test.json", "w", encoding="utf-8") as file:
            json.dump(users, file, ensure_ascii=None)