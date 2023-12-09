import requests
import os
import argparse
from dotenv import load_dotenv

from Download_images import download_photo


def get_extension(link):
    extension = os.path.splitext(link)[1]
    return extension


def pictory_day_nasa(key_NASA, count):
    payload = {
        "api_key": key_NASA,
        "count": count
    }
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    response_nasa = requests.get(url_nasa, params=payload)
    for image_number, img in enumerate(response_nasa.json()):
        img_link = img["url"]
        extension = get_extension(img_link)
        filename = f"NASA_photo_{image_number}{extension}"
        download_photo(filename, img_link)


def main():

    load_dotenv()
    key_NASA = os.getenv("KEY_NASA")

    parser = argparse.ArgumentParser(
        description='получение фото космоса'
    )
    parser.add_argument('--c', '--count', type= int, help='количество фото', default=40)
    args = parser.parse_args()

    pictory_day_nasa(key_NASA, args.count)


if __name__ == '__main__':
    main()