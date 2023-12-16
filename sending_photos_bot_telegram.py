import os
import random
import telegram
import argparse
from time import sleep
from dotenv import load_dotenv


def main():
    
    time_delay = 4

    parser = argparse.ArgumentParser(
        description='отправка фотографий в telegram канал'
    )
    parser.add_argument('--pt', '--periodicity_time', type= int, help='время задержни сводки фото в секундах', default=14400)
    args = parser.parse_args()
    
    load_dotenv()
    tg_bot_key = os.getenv("TG_BOT_KEY")
    chanal_name = os.getenv("CHANNEL_NAME")

    while True:
        bot = telegram.Bot(token=tg_bot_key)
        bot.send_message(text='Hi John!', chat_id=chanal_name)
        folder = os.walk('images')
        for files in folder:
            files = files[2]
            all_files = os.walk("images")

            for array_of_files in all_files:
                folder, nested_folder, files = array_of_files
                random.shuffle(files)

                for tg_file_image in files:
                    bot.send_document(chat_id=chanal_name, document=open(f"images/{tg_file_image}", "rb"))
                    sleep(time_delay)
        sleep(args.periodicity_time)


if __name__ == '__main__':
    main()