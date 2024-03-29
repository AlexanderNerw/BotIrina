from support.config import Dispatcher, InlineKeyboardButton, InlineKeyboardMarkup, dp, bot, general_text, start_sign_up, \
      CallbackQuery, exceptions, KeyboardButton, CHAT_PRIVATE, CHAT_GROUP, ReplyKeyboardRemove, ReplyKeyboardMarkup, ADMIN
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from general.support.querry_db import db
from handlers.menu import toMenu


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    start = State()
    lang = State()
    name = State()
    gender = State()

##################################### - СТАРТ ЛИЧНОГО ЧАТА - #######################################################

@dp.message_handler(CHAT_PRIVATE, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start(message: Message) -> None:
    try:    


        if (not db.user_in_database(message.chat.id)) or (not db.user_online(message.chat.id)):  # Пользователя нет в БД или он не онлайн

            db.add_subs(message.chat.id)
            if message.from_user.language_code in ['ru','uk']:
                await message.answer(   general_text[f'{message.from_user.language_code}_hello'] + f",<b> {message.chat.first_name}</b>! 😉"
                                     +  start_sign_up[f'{message.from_user.language_code}_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸" if message.from_user.language_code == 'ru' else "Регiстрацiя 🔸", callback_data='Регистрация 🔸')))

            else: await message.answer( general_text['ru_hello'] + f",<b> {message.chat.first_name}</b>! 😉"
                                     +  start_sign_up['ru_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸", callback_data='Регистрация 🔸')))
            await ProfileStateGroup.start.set()

        else:  # Пользователь есть в БД
            lang = db.getting(message.chat.id, 'language')
            await message.answer(f"{general_text[f'{lang}_hello']}, <b>{db.getting(message.chat.id, 'username')}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await toMenu(message)

    except Exception as ex: await exceptions("sign_up.py", 'start', ex)

#==============================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text = 'Регистрация 🔸', state='*')
async def start_reg(call : CallbackQuery) -> None:
    try:
        if (not db.user_in_database(call.message.chat.id)) or (not db.user_online(call.message.chat.id)):  # Пользователя нет в БД или он не онлайн
            choice_lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*["Русский", "Українська"])

            await bot.send_message(call.message.chat.id, start_sign_up[f'ru_start_1/3'], parse_mode='html', reply_markup=choice_lang_kb)
            await ProfileStateGroup.start.set(), await call.answer()
            await ProfileStateGroup.next()

    except Exception as ex: await exceptions("sign_up.py", 'start_reg', ex)

#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.lang)
async def start_lang(message: Message, state: FSMContext) -> None:
    try:
        
        if message.text in ['Русский', 'Українська 🇺🇦']:

            async with state.proxy() as data:
                data['lang'] = 'ru' if message.text == 'Русский' else 'uk' 

            db.adding(message.chat.id, 'language', data['lang'])
            await message.answer(start_sign_up[f"{data['lang']}_start_2/3"], parse_mode='html',
            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(message.chat.first_name)))
            await ProfileStateGroup.next()

        else:
            await message.reply(start_sign_up['ru_dont_know_start'])

    except Exception as ex: await exceptions("sign_up.py", 'start_lang', ex)

#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.name)
async def start_name(message: Message, state: FSMContext) -> None:

    try:
        async with state.proxy() as data: 
            if len(message.text) <= 30:
                db.adding(message.from_user.id, 'username', message.text)
                buttons = ["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"] if data['lang'] == 'ru' else ["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"]

                await message.answer(start_sign_up[f"{data['lang']}_start_3/3"], parse_mode='html',
                reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons))
                await ProfileStateGroup.next()

            else:
                await message.reply(start_sign_up[f"{data['lang']}_start_too_long_name"])

    except Exception as ex: await exceptions("sign_up.py", 'start_name', ex)

#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.gender)
async def start_gender(message: Message, state: FSMContext) -> None:
    try:
        if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️', "Я девушка 👱🏼‍♀️", "Я дівчина 👱🏼‍♀️"]:

            async with state.proxy() as data: 
                db.adding(message.from_user.id, 'gender', 'man' if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️'] else 'woman')
                await bot.send_message(ADMIN, '[INFO] Новый зарегистрированный пользователь')
                await message.answer(general_text[f"{data['lang']}_to_menu"], reply_markup=ReplyKeyboardRemove())
                db.adding(message.chat.id, 'status', 1)
                await state.finish(), await toMenu(message)

        else:
            await message.reply(start_sign_up[f"{data['lang']}_dont_know_start"])

    except Exception as ex: await exceptions("sign_up.py", 'start_gender', ex)


##################################### - СТАРТ ГРУППОВОГО ЧАТА -  ###################################################

@dp.message_handler(CHAT_GROUP, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start_group(message: Message, state: FSMContext) -> None:
    try:    
        if (not db.user_in_database(message.chat.id)) or (not db.user_online(message.chat.id)):  # Пользователя нет в БД или он не онлайн

            db.add_subs(message.chat.id)
            if message.from_user.language_code in ['ru','uk']:
                await message.answer(       message.from_user.id,
                                            general_text[f'{message.from_user.language_code}_hello'] + f" <b>{message.chat.first_name}</b>! 😉"
                                         +  start_sign_up[f'{message.from_user.language_code}_bot_start'], parse_mode='html', reply_markup=
                                            InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                            InlineKeyboardButton("Регистрация 🔸" if message.from_user.language_code == 'ru' else "Регiстрацiя 🔸", callback_data='Регистрация 🔸')))

            else: await message.answer(     general_text[f'ru_hello'] + f"<b>{message.chat.first_name}</b>! 😉"
                                         +  start_sign_up['ru_bot_start'], parse_mode='html', reply_markup=
                                            InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                            InlineKeyboardButton("Регистрация 🔸", callback_data='Регистрация 🔸')))

            await ProfileStateGroup.start.set()

        else:  # Пользователь есть в БД

            lang = db.getting(message.from_user.id, 'language')
            await message.answer(f"{general_text[f'{lang}_hello']}, <b>{db.getting(message.from_user.id, 'username')}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await toMenu(message)

    except Exception as ex: await exceptions("sign_up.py", 'start_group', ex)


def register(dp : Dispatcher):
    dp.register_message_handler(start, CommandStart())
    dp.register_callback_query_handler(start_reg, text = 'Регистрация 🔸', state='*')
    dp.register_message_handler(start_lang, content_types=['text'], state=ProfileStateGroup.lang)
    dp.register_message_handler(start_name, content_types=['text'], state=ProfileStateGroup.name)
    dp.register_message_handler(start_gender, content_types=['text'], state=ProfileStateGroup.gender)