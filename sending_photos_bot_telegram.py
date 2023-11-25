import os
import telegram
from dotenv import load_dotenv








def main():
    load_dotenv()
    key_bot = os.getenv("KEY_BOT")
    chanal_name = os.getenv("CHANNEL_NAME")
    bot = telegram.Bot(token=key_bot)
    bot.send_message(text='Hi John!', chat_id=chanal_name)
    


if __name__ == '__main__':
    main()