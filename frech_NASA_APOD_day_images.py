import requests
import os

from Download_images import download_photo


def get_extension(link):
    extension = os.path.splitext(link)[1]
    return extension


def pictory_day_nasa():
    payload = {
        "api_key": "5HF3znYx16boQ8oDql9SGU0swAl70NtRgA9GTTnz",
        "count": 40
    }
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    response_nasa = requests.get(url_nasa, params=payload)
    for image_number, img in enumerate(response_nasa.json()):
        img_link = img["url"]
        extension = get_extension(img_link)
        filename = f"NASA_photo_{image_number}{extension}"
        download_photo(filename, img_link)


def main():
    pictory_day_nasa()


if __name__ == '__main__':
    main()