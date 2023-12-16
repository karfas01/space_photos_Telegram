import requests
import os
import argparse
from dotenv import load_dotenv

from Download_images import download_photo


def get_extension(link):
    extension = os.path.splitext(link)[1]
    return extension


def get_nasa_pichture(key_nasa, count):
    payload = {
        "api_key": key_nasa,
        "count": count
    }
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    nasa_api_response = requests.get(nasa_url, params=payload)
    for image_number, img in enumerate(nasa_api_response.json()):
        img_link = img["url"]
        extension = get_extension(img_link)
        filename = f"NASA_photo_{image_number}{extension}"
        download_photo(filename, img_link)


def main():

    load_dotenv()
    key_nasa = os.getenv("KEY_NASA")

    parser = argparse.ArgumentParser(
        description='получение фото космоса'
    )
    parser.add_argument('--count', type= int, help='количество фото', default=40)
    args = parser.parse_args()

    get_nasa_pichture(key_nasa, args.count)


if __name__ == '__main__':
    main()