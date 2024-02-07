import pymysql, os, time, asyncio
from dotenv import load_dotenv
from support.config import exceptions


class QuerryDB: # Database and Querry 

    def __init__(self):
        """ Connection to DataBase """

        try:
            load_dotenv()
            self.connection = pymysql.connect(
                host=       os.getenv('host'),
                port=       3306,
                user=       os.getenv('user'),
                password=   os.getenv('password'),
                database=   os.getenv('database'), # pandabase
                cursorclass=pymysql.cursors.DictCursor)

            self.table_with_user_info = 'user_info' 
            self.table_with_chat_info = 'chat_info' 

            print("querry_db.py [INFO] Database Succes Connection")

            # with self.connection.cursor() as cursor:

            #     cursor.execute( f"CREATE TABLE IF NOT EXISTS {self.table_with_chat_info} \
            #                     (id INT NOT NULL AUTO_INCREMENT, \
            #                     chat_id VARCHAR(50) NOT NULL, \
            #                     user_id VARCHAR(50) NOT NULL, \
            #                     specialist_id VARCHAR(13) NOT NULL, \
            #                     status_chat VARCHAR(13) DEFAULT 0, PRIMARY KEY (id));" )


            #     cursor.execute( f"CREATE TABLE IF NOT EXISTS {self.table_with_user_info} \
            #                     (id INT NOT NULL AUTO_INCREMENT, \
            #                     user_id VARCHAR(50) NOT NULL, \
            #                     fk_role INT NULL, \                      
            #                     status TINYINT(1) DEFAULT 0, \
            #                     phone VARCHAR(50) NULL, \
            #                     language VARCHAR(50) DEFAULT 'uk', \
            #                     specialist_id VARCHAR(50) NULL, \
            #                     chat_id VARCHAR(50), \
            #                     PRIMARY KEY (id));")
                
            #     try: self.connection.commit(), self.connection.close()
            #     except Exception as ex: print(f"[INFO] querry_db.py, Database(init: commit&close):\n{ex}")

        except Exception as ex: 
            print(f"[INFO] querry_db.py, Database(init):\n{ex}")

####################### СТАРТОВЫЕ ХЕРНИ #################################

    async def user_have_this(self, get: str,  where: str, where_value: str|int, database = 'user_info', one_info = True):
        """
        Проверяем есть ли уже юзер в базе.
        Возвращает True если его user_id есть в базе, и False если нет.
        """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT {get} FROM `{database}` WHERE `{where}` = {where_value};')
                if one_info:
                    result = cursor.fetchone()
                    return False if result == None else True
            
                else: 
                    result = cursor.fetchone()
                    return False if result == None else True          

        except Exception as ex: await exceptions("querry_db.py", 'Database: (user_in_db)', ex)

        finally: self.connection.close()

# ------------------------------------------------

    async def add_user(self, user_id: str|int, phone: str|int):
        """
        Добавление нового юзера. 
        Проверяет есть ли юзер в боте, после чего добавляет в бд.
        """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT * FROM {self.table_with_user_info} WHERE user_id = {user_id};')
                result = cursor.fetchone()                
                if (True if result == None else False):
                    cursor.execute(f"INSERT INTO {self.table_with_user_info}(`user_id`,`phone`) VALUES ({user_id}, {phone});")
                    return True
                else: return False

        except Exception as ex:
            await exceptions("querry_db.py", 'Database: (add_user)', ex)
            return False
        
        finally: self.connection.commit(), self.connection.close()

####################### ДОБАВЛЕНИЕ И ПОЛУЧЕНИЕ ХЕРНИ #################################

    async def add_info(self, set: str, value: str|int, where: str, where_value: str|int, database = 'user_info'):
        """
        Добавление какой-то херни.
        Обновление заданой информации (value) в заданную колонку (set) заданной таблицы (database).
        Где в колонке (where) есть значение (where_value)
        """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'UPDATE {database} SET `{set}` = "{value}" WHERE `{where}` = {where_value};')
                return True

        except Exception as ex:
            await exceptions("querry_db.py", 'Database: (add_info)', ex)
            return False
        
        finally: self.connection.commit(), self.connection.close()

# ------------------------------------------------

    async def get_info(self, get: str, where: str, where_value: str|int, database = 'user_info', one_info = True):
        """
        Получение какой-то херни.
        Получает заданную информацию (set) в заданной бд (database) где (user_id)
        """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT {get} FROM {database} WHERE {where} = {where_value}')
            if one_info:
                result = cursor.fetchone()
                if result != None: return result[get] 
                else: return ''
            else: 
                result = cursor.fetchall()
                return result
            
        except Exception as ex: await exceptions("querry_db.py", 'Database: (get_info)', ex)

        finally: self.connection.close()

    async def get_all_info(self, get: str, database = 'user_info'):
        """
        Получение какой-то херни.
        Получает заданную информацию (set) в заданной бд (database) где (user_id)
        """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT {get} FROM {database}')
                result = cursor.fetchall()
                return result
                      
        except Exception as ex: await exceptions("querry_db.py", 'Database: (get_info)', ex)

        finally: self.connection.close()

# ------------------------------------------------

# Cоединение с БД
db = QuerryDB()

#print(db.get_all_info())
#db.addingInEnd(1082803262, 'text_to_send', 5)
# a.delete_person('1082803262')
