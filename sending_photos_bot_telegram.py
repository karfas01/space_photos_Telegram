import os
import telegram
from dotenv import load_dotenv



def main():
    load_dotenv()
    key_bot = os.getenv("KEY_BOT")
    chanal_name = os.getenv("CHANNEL_NAME")
    bot = telegram.Bot(token=key_bot)
    bot.send_message(text='Hi John!', chat_id=chanal_name)

    folder = os.walk('images')
    for files in folder:
        for file_image in files[2]:
            bot.send_document(chat_id=chanal_name, document=open(f"images/{file_image}", "rb"))

if __name__ == '__main__':
    main()