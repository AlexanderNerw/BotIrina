from aiogram.dispatcher.filters.builtin import ChatTypeFilter, ChatType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging, time, os
from dotenv import load_dotenv


# Уровень логов
logging.basicConfig(level=logging.INFO, format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s')
storage = MemoryStorage()
load_dotenv()

#===================================================================#   INFO

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv('ADMIN')

LOCAL_DATABASE = { '1082803262' : 'ru' }

CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)


api_id = 29156484
api_hash = "25699c6ea0e0283ace42b5939e3b8f80"

#, api_id=api_id, api_hash=api_hash, bot_token=TOKEN

#app = Client('Olexander')

#====================================================================================================#   ERRORS  
    
async def exceptions(file: str, func: str, exception: str):            
    try:                                    
        await bot.send_message(ADMIN, f"[ERROR] File: {file} | Func: {func}() \nError: {exception}")
        print(f"[ERROR] [{time.asctime()}] File: {file} | Func: {func}: \nError: {exception}")         
    
    except Exception as ex:
        await bot.send_message(ADMIN, f"[ERROR] File: config.py | Func: exceptions() \nError: {ex}")
        print(f"[ERROR] [{time.asctime()}] File: config.py | Func: exceptions() \nError: {ex}")

#====================================================================================================#   BOT INFO

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = storage)