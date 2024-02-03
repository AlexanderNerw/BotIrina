from aiogram import Bot, Dispatcher
import logging, os
from dotenv import load_dotenv

# Уровень логов
logging.basicConfig(level=logging.INFO, format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s')
load_dotenv()

#===================================================================#   INFO

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv('ADMIN')

LOCAL_DATABASE = { '1082803262' : 'ru' }

#====================================================================================================#   BOT INFO

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)