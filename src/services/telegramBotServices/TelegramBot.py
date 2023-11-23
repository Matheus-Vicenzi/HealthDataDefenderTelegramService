from telegram import Bot

from infra.EnviromentConstants import TELEGRAM_BOT_KEY, MY_TELEGRAM_ID

async def send_message():
    print("TELEGRAM_BOT_KEY: ", TELEGRAM_BOT_KEY)
    print("MY_TELEGRAM_ID: ", MY_TELEGRAM_ID)
    bot = Bot(TELEGRAM_BOT_KEY)
    await bot.send_message(chat_id=MY_TELEGRAM_ID, text='Hello, World!')
    
    