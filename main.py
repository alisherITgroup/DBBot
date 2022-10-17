from aiogram import Bot, Dispatcher, types, executor
import sqlite3
connector = sqlite3.connect('tgbot.db')
cursor = connector.cursor()


BOT_TOKEN = "5574137451:AAFUuTct94Kh2iYuQ2Xy2j9ocNiclYaBVzQ"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_(message: types.Message):
    tg_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    cursor.execute("""
        SELECT * FROM users;
    """)
    for i in cursor.fetchall():
        if tg_id not in i:

            cursor.execute(f"""
                INSERT INTO users(tg_id, username, first_name) VALUES('{tg_id}', '{username}', '{first_name}');
                """)
            connector.commit()
        else:
            pass

    await message.answer("Assalomu alaykum")


@dp.message_handler(commands='admin')
async def admin(message: types.Message):
    cursor.execute("""
        SELECT * FROM users;
    """)
    await message.answer(cursor.fetchall())

executor.start_polling(dp, skip_updates=True)
