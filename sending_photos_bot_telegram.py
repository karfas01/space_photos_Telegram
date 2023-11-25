import os
import telegram
from dotenv import load_dotenv








def main():
    load_dotenv()
    key_bot = os.getenv("KEY_BOT")
    bot = telegram.Bot(token=key_bot)
    print(bot.get_me())
    


if __name__ == '__main__':
    main()