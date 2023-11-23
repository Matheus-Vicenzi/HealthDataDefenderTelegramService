from dotenv import load_dotenv
import os


base_dir = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(base_dir, "../../.env")

load_dotenv(dotenv_path=env_path)

TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_API_KEY")
MY_TELEGRAM_ID = os.getenv("MY_TELEGRAM_ID")