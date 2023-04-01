import os
import openai
import config
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import json

openai.api_key = config.OPENAI_API_KEY
telegram_token = config.TG_TOKEN

bot = Bot(telegram_token)
dp = Dispatcher(bot=bot)


async def on_startup(_):
  print("Bot is active!")
  with open("users.json", "r", encoding="utf-8") as read_file:
    users = json.load(read_file)
  for i in range(len(users) - 1):
    if (users[f"{i}"]["user_id"] == users[f"{i + 1}"]["user_id"]):
      print("Обнаружен повторный пользователь")
      del users[f"{i + 1}"]
      with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=None)

@dp.message_handler(commands=["start"])
async def send_message(msg: types.Message):
  bot_name = await bot.get_me()
  await msg.answer(
    f"Приветствую, <b>{msg.from_user.full_name}</b>!\nЯ - <b>{bot_name.first_name}</b>,"
    f" виртуальный помощник для решения домашних заданий. Могу решить любые задачи, объяснить тему, "
    f"написать сочинение и много другое. Завай вопросы!",
    parse_mode="html",)
  await msg.delete()
  #users = {"user_id": [], }
  with open("users.json", "r", encoding="utf-8") as read_file:
    users = json.load(read_file)
    # user_id = []
    # user_name = []
    # user_id = users["user_id"]
    # user_name = users["username"]
  # print(len(users))
  print(users)
  # print(users["0"])
  user_a = bool
  user_a = False
  for a in range(len(users)):
    if (msg.from_user.id in users[f"{a}"]["user_id"]):
      print("Пользователь уже есть")
      user_a == True
  #print("Промежуточный этап")

  if user_a == False:
      print("Новый пользователь")
      # users["1"]["user_id"] = msg.from_user.id
      # users["1"]["username"] = msg.from_user.full_name
      # users.update({len(users):{("user_id", msg.from_user.id), ("username", msg.from_user.full_name)}})
      users.update({len(users):{"user_id": [msg.from_user.id], "username": msg.from_user.full_name}})
      # user_id.append(msg.from_user.id)
      # user_name.append(msg.from_user.full_name)
      # users["user_id"] = user_id
      # users["username"] = user_name
      with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=None)

@dp.message_handler()
async def send_message(msg: types.Message):
  print('User: ', msg.from_user.id, msg.from_user.full_name)
  if msg.text.lower() == "привет" or msg.text.lower() == "ку":
    await msg.answer(
      f"Привет, <b>{msg.from_user.full_name}</b>! "
      f"С чем помочь тебе сегодня?",
      parse_mode="html", )
  else:
    try:
      edit_msg = await bot.send_message(msg.chat.id, text="Формируется ответ...", parse_mode="html")
      prompt = f"Act like a high school teacher. " \
               f"I will ask you to help with school assignments, you must give solutions " \
               f"for problems, understand school material and help me in every possible way." \
               f"Think und explain step by step. Answer in Russian: {msg.text}"
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        temperature=0.7,
        max_tokens=(4000-len(prompt)),
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
      )
      #print(response)
      #print(response['choices'][0]['text'])
      #print(len(response['choices'][0]['text']))

      await edit_msg.edit_text(response['choices'][0]['text'] , parse_mode="html")
    except Exception as e:
      print('User: ', msg.from_user.id, f'\nError: ', repr(e))
      await bot.send_message(msg.chat.id, f'Произошла ошибка. Попробуйте ещё раз...\nError: {repr(e)}')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)