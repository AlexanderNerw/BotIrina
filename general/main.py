from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from pyrogram import Client, filters
from support.querry_db import db
from support.config import bot, dp, ADMIN, CHAT_PRIVATE, exceptions
from aiogram.dispatcher.filters.builtin import CommandStart
from support.dialogs import start_bot
import aioschedule, asyncio

lang_db = { '1082803262' : 'uk' }

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

# @dp.message_handler(CHAT_PRIVATE, content_types=types.Message)
# async def start(message: Message) -> None:
#     print(message)

@dp.message_handler(CHAT_PRIVATE, commands="cucumber")
async def cucumber(message: Message):
    a = await db.get_all_info(("user_id, language"))
    #await bot.send_message(message.from_user.id, a)
    count = 0

    while len(a) > count:
        print(a[count]['user_id'], a[count]['language'])
        count+=1

@dp.message_handler(CHAT_PRIVATE, content_types=types.ContentType.CONTACT)
async def reg_number(message: types.ContentType.CONTACT):
    try:

        if  not (await db.user_have_this('*','user_id', message.from_user.id, one_info=False)):
            if (message.from_user.id == message.contact.user_id): 
                
                if not (await db.user_have_this('phone', 'phone', message.contact.phone_number, 'accounts')):

                    await db.add_user(message.from_user.id, message.contact.phone_number)
                    await bot.send_message(message.from_user.id, f"{start_bot[f'hello_{lang_db[message.from_user.id]}']}, {await db.get_info('name', 'phone', f'+{message.contact.phone_number}', 'accounts')} \n\n{start_bot[f'auth_phone_{lang_db[message.from_user.id]}']}")

                else:
                    await bot.send_message(message.from_user.id, start_bot[f"non_auth_phone_{lang_db[message.from_user.id]}"])
            else: 
                button = KeyboardButton(start_bot[f"send_phone_{lang_db[message.from_user.id]}"], request_contact=True)
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                keyboard.add(button)

                await bot.send_message(message.from_user.id, "Это не твой контакт утырок, давай заново.", reply_markup = keyboard)
        else:
            await bot.send_message(message.from_user.id, "Я не розумію що ти хочеш")

    except Exception as ex: 
        await exceptions("main.py", 'reg_number', ex)


@dp.message_handler(CHAT_PRIVATE, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start(message: Message) -> None:
    try:
        # if (await db.user_have_this('is_specialist', 'phone', f"+{message.get_args()}")):
        #     await bot.send_message(message.chat.id, 'Нормально')
        # else: 
        #     print("Нет аргументов")
        ############################################### Проверяем есть ли юзер в боте

        if (await db.user_have_this('*','user_id', message.from_user.id, one_info=False)):

            await bot.send_message(message.chat.id, start_bot[f"again_start_bot_{message.from_user.language_code}"], parse_mode='html')

        ################################################# Если изера ещё нет в боте
        else: 

            await bot.send_message(message.chat.id, start_bot[f"start_bot_{message.from_user.language_code}"], reply_markup= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                KeyboardButton(start_bot[f"send_phone_{message.from_user.language_code}"], request_contact=True)))

    except Exception as ex: 
        await exceptions("main.py", 'start', ex)


async def on_startup(dp):

    a = await db.get_all_info(("user_id, language"))
    count = 0
    while len(a) > count:
        lang_db.update( {a[count]['user_id']: a[count]['language']} )
        count+=1

    #await bot.send_message(ADMIN, "Ну чё, я перезапустился")

async def on_shutdown(dp):
    pass
    #await bot.send_message(ADMIN, "Ну я ушёл, всё")
    

if __name__ == '__main__': 
    executor.start_polling(dp, on_startup=on_startup, 
                           on_shutdown=on_shutdown, 
                           skip_updates= True, 
                           reset_webhook=True)
    
    executor.start_webhook(dp, )