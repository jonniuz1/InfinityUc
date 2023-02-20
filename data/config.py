from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS = env.list("CHANNELS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:Asdfvcxz1@infinityucbotdb.cat1mvipi4nl.ap-northeast-1.rds.amazonaws.com:5432/InfinityucBot_DB'
# SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:password@hostname:port/db_name'
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
