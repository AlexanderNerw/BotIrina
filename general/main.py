from aiogram import Bot, Dispatcher, types, executor
from pyrogram import Client, filters
import support.querry_db as db
from dotenv import load_dotenv
from config import bot, dp, os, ADMIN, CHAT_PRIVATE, CHAT_GROUP

load_dotenv()

#@app.on_message(filters.text & filters.private)
#async def main(_, msg):
    #print(msg)
    #a = await app.create_group("Тестовый авто-чат", [1082803262, 6147145237])
    #b = await app.create_chat_invite_link(a.id, "Тестовый авто-чат")
    #await app.send_message(1082803262, b.invite_link)
    #await appMe.leave_chat(a.id, False)
    #b = await appMe.get_chat(a.id)
    #await appMe.send_message(1082803262, b)

#app.run()


# @dp.message_handler()
# async def echo(message: types.Message):
#     await bot.send_message(message.chat.id, message)
#     ids = [1082803262, 5287350422]
#     await app.create_group(ids, "Группа тестовая")
#     #print(message.chat.id)
 

async def on_startup(dp):
    await bot.delete_webhook()
    await bot.send_message(ADMIN, "Ну чё, я перезапустился")

async def on_shutdown(dp):
    await bot.send_message(ADMIN, "Ну я ушёл, всё")
    

if __name__ == '__main__': 
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates= True)