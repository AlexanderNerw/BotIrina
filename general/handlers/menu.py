from support.config import dp, bot, general_text, board_menu, CHAT_PRIVATE, CHAT_GROUP, exceptions, CallbackQuery
import handlers.sign_up
from aiogram.dispatcher import FSMContext
from general.support.querry_db import db


######################################################################################### - ГЛАВНОЕ МЕНЮ ЛИЧНОГО ЧАТА
@dp.message_handler(CHAT_PRIVATE, commands=['menu'])                                   ##   ГЛАВНОЕ МЕНЮ
async def toMenu(message) -> None: 
    try:
        if (db.user_online(message.chat.id)):

            await bot.send_message(message.chat.id, general_text[f"{db.getting(message.chat.id, 'language')}_menu_text"],
                parse_mode='html', reply_markup = board_menu[db.getting(message.chat.id, 'language')])

        else: await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)

    except Exception as ex: await exceptions("menu.py", 'toMenu', ex)


@dp.callback_query_handler(CHAT_PRIVATE, text="toMenu")                                ##   ГЛАВНОЕ МЕНЮ БЕЗ ИЗМЕНЕНИЙ
async def inline_toMenu(call: CallbackQuery) -> None:
    try: await toMenu(call.message), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_toMenu', ex)

@dp.callback_query_handler(CHAT_PRIVATE, text='toMenu_without')                        ##   ГЛАВНОЕ МЕНЮ С ИЗМЕНЕНИЕМ
async def toMenu_without(c: CallbackQuery) -> None:
    try:

        if (db.user_online(c.message.chat.id)):

            await bot.edit_message_text(general_text[f"{db.getting(c.message.chat.id, 'language')}_menu_text"],
                c.message.chat.id, c.message.message_id, parse_mode='html', reply_markup = board_menu[db.getting(c.message.chat.id, 'language')])

        else:
            await bot.send_message(c.message.chat.id, 'Сначала зарегистрируйся 🙂:')
            await handlers.sign_up.start(c.message, FSMContext)

    except Exception as ex: await exceptions("menu.py", 'toMenuWithout', ex)


######################################################################################### - ГЛАВНОЕ МЕНЮ ГРУППОВОГО ЧАТА
@dp.message_handler(CHAT_GROUP, commands=['menu'])                                     ##   ГЛАВНОЕ МЕНЮ ГРУППОВОГО ЧАТА
async def toMenu_group(message) -> None: 
    try:
        print(message)
        if (db.user_online(message.chat.id)):

            await bot.send_message(message.chat.id, general_text[f"{db.getting(message.chat.id, 'language')}_menu_text"],
                parse_mode='html', reply_markup = board_menu[db.getting(message.chat.id, 'language')])

        else: await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)

    except Exception as ex: await exceptions("menu.py", 'toMenu_group', ex)
