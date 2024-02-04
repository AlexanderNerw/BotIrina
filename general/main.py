from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import aiogram
from pyrogram import Client, filters
from support.querry_db import db
from support.config import bot, dp, ADMIN, CHAT_PRIVATE
from aiogram.dispatcher.filters.builtin import CommandStart, IsSenderContact

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

@dp.message_handler(CHAT_PRIVATE, content_types=types.ContentType.CONTACT)
async def handle_message(message: types.ContentType.CONTACT):

    if not (bool(await db.get_info('status', 'user_id', message.from_user.id))):
        if (message.from_user.id == message.contact.user_id): 
            
            if (await db.user_have_this('phone', 'phone', message.contact.phone_number, 'accounts')):
                
                await db.add_info(("'phone','status'"), (f"'{message.contact.phone_number}', 1"), 'chat_id', message.from_user.id)
                await bot.send_message(message.from_user.id, "Привет, {name}!\nВот твои функции.")

            else:
                await bot.send_message(message.from_user.id, "Вижу ты ещё не зареган у нас. Держи ссылочку и зарегайся: \
                                    talkind.me/auth/sing-up \n\nПосле регистрации нужно подвязать свой номер телефона в настройках,\
                                    после чего снова прислать мне свой контакт, и ты сможешь пользоваться этим ботом :)")
        else: 
            button = KeyboardButton("Отправить номер телефона", request_contact=True)
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            keyboard.add(button)

            await bot.send_message(message.from_user.id, "Это не твой контакт утырок, давай заново.", reply_markup = keyboard)
    else:
        await bot.send_message(message.from_user.id, "Я не розумію що ти хочеш")


@dp.message_handler(CHAT_PRIVATE, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start(message: Message) -> None:
    #try:

        button = KeyboardButton("Отправить номер телефона", request_contact=True)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(button)
        ################################################ Проверяем есть ли юзер в боте
        if (await db.user_have_this('*','user_id', message.chat.id)):
            await bot.send_message(message.chat.id, f'<b>Привет снова :D</b>', reply_markup= keyboard, parse_mode='html')

        ################################################# Если изера ещё нет в боте
        else: 
            await db.add_user(message.from_user.id)
            await bot.send_message(message.chat.id, f'Ты теперь в базе данных.')


async def on_startup(dp):
    pass
    #await bot.send_message(ADMIN, "Ну чё, я перезапустился")

async def on_shutdown(dp):
    pass
    #await bot.send_message(ADMIN, "Ну я ушёл, всё")
    

if __name__ == '__main__': 
    executor.start_polling(dp, on_startup=on_startup, 
                           on_shutdown=on_shutdown, 
                           skip_updates= True, 
                           reset_webhook=True)