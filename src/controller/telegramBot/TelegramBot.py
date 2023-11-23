from fastapi import FastAPI, HTTPException
from services.telegramBotServices.TelegramBot import send_message 

app_bot_telegram = FastAPI()

@app_bot_telegram.get("/teste")
async def read_root():
    try:
        await send_message()
        return {"Status": "Executado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))