import os
from dotenv import load_dotenv
import requests

from Download_images import download_photo


def pictory_epic(key_nasa):

    number_of_repetitions = 5

    payload = {"api_key": key_nasa}
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    response_epic = requests.get(epic_url, params=payload)
    response_epic.raise_for_status()
    decrypted_response_epic = response_epic.json()
    for epic_picture_number in range(number_of_repetitions):
        epic_picture = decrypted_response_epic[epic_picture_number]
        img_name = f"{epic_picture['image']}.png"
        date = epic_picture["date"].split()[0]
        date_year = date.split("-")[0]
        date_month = date.split("-")[1]
        date_day = date.split("-")[2]
        epic_url_img = f"https://api.nasa.gov/EPIC/archive/natural/{date_year}/{date_month}/{date_day}/png/{img_name}"
        filename = f"EPIC_picture_{epic_picture_number}.png"
        download_photo(filename, epic_url_img, payload)


def main():
    load_dotenv()
    key_nasa = os.getenv("KEY_NASA")
    pictory_epic(key_nasa)


if __name__ == '__main__':
    main()