#from aiogram import Dispatcher, types, executor
#import asyncio
#from aiogram import Bot, Dispatcher
import logging, os
from dotenv import load_dotenv
from pyrogram import Client, filters
import pyrogram
from pyrogram.types import ChatPermissions

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv('ADMIN')

api_id = 29156484
api_hash = "25699c6ea0e0283ace42b5939e3b8f80"

#, api_id=api_id, api_hash=api_hash, bot_token=TOKEN

app = Client('Olexander')

@app.on_message(filters.text & filters.private)
async def main(_, msg):
    #print(msg)
    #a = await appMe.create_group("Тестовый авто-чат", [1082803262, 6147145237])
    print( await app.create_supergroup("Тестовый авто-суперчат", "Тестовый авто-суперчат") )
    #b = await app.create_chat_invite_link(a.id, "Тестовый авто-чат")
    #await app.send_message(1082803262, b.invite_link)
    #await appMe.leave_chat(a.id, False)
    #b = await appMe.get_chat(a.id)
    #await appMe.send_message(1082803262, b)


app.run()

# async def main():
#     async with app:
#         await app.send_message(1082803262, "Hi!")
#         ids = [1082803262, 5287350422]
#         print( pyrogram.raw.functions.messages.CreateChat(users=[1082803262, 5287350422], title="AfsASr134r114r"))


# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.chat.id, message)
#     ids = [1082803262, 5287350422]
#     await app.create_group(ids, "Группа тестовая")
#     #print(message.chat.id)
 

# async def on_startup(dp):
#     await bot.delete_webhook()
    #await bot.create_chat_invite_link(chat_id=1082803262)
    #await bot.send_message(ADMIN, "Ну чё ты лох, я перезапустился")
    

# if __name__ == '__main__': 
#     asyncio.run(executor.start_polling(dp, on_startup=on_startup, skip_updates= True))