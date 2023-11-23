import os
from dotenv import load_dotenv
import requests

from Download_images import download_photo


def pictory_epic(key_NASA):
    payload = {"api_key": key_NASA}
    url_epic = "https://api.nasa.gov/EPIC/api/natural/images"
    response_epic = requests.get(url_epic, params=payload)
    for epic_picture_number in range(5):
        epic_picture = response_epic.json()[epic_picture_number]
        original_name = epic_picture["image"].split("_")
        original_name_1 = original_name[0]
        original_name_3 = original_name[2]
        file_name_img = f"{original_name_1}_1b_{original_name_3}.png"
        date = epic_picture["date"].split()[0]
        date_year = date.split("-")[0]
        date_month = date.split("-")[1]
        date_day = date.split("-")[2]
        url_epic_img = f"https://api.nasa.gov/EPIC/archive/natural/{date_year}/{date_month}/{date_day}/png/{file_name_img}"
        filename = f"EPIC_picture_{epic_picture_number}.png"
        download_photo(filename, url_epic_img, payload)


def main():
    load_dotenv()
    key_NASA = os.getenv("KEY_NASA")
    pictory_epic(key_NASA)


if __name__ == '__main__':
    main()