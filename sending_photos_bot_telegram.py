import os
import random
import telegram
import argparse
from time import sleep
from dotenv import load_dotenv


def main():
    
    parser = argparse.ArgumentParser(
        description='отправка фотографий в telegram канал'
    )
    parser.add_argument('--sst', '--sleep_summaries_time', type= int, help='время задержни сводки фото в секундах', default=14400)
    args = parser.parse_args()
    
    load_dotenv()
    key_bot = os.getenv("KEY_BOT")
    chanal_name = os.getenv("CHANNEL_NAME")

    while True:
        bot = telegram.Bot(token=key_bot)
        bot.send_message(text='Hi John!', chat_id=chanal_name)
        folder = os.walk('images')
        for files in folder:
            files = files[2]
            all_files = os.walk("images")

            for array_of_files in all_files:
                folder, nested_folder, files = array_of_files
                random.shuffle(files)

                for file_image in files:
                    bot.send_document(chat_id=chanal_name, document=open(f"images/{file_image}", "rb"))
                    sleep(4)
        sleep(args.sleep_summaries_time)


if __name__ == '__main__':
    main()