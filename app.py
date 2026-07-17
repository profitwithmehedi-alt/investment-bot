import logging
from telegram.ext import Application
from config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    print("✅ Investment Bot Started Successfully...")

    app.run_polling()

if __name__ == "__main__":
    main()