from fastapi import FastAPI
from controller.telegramBot.TelegramBot import app_bot_telegram

main_app = FastAPI()
main_app.mount("/telegram", app_bot_telegram)