import requests
import os


def download_photo(filename, url, payload=""):

    foldername = 'images'
    full_path = f"{foldername}/{filename}"

    if not os.path.isdir(foldername):
        os.mkdir(foldername)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(full_path, 'wb') as file:
        file.write(response.content)


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


def pictory_epic():
    payload = {"api_key": "5HF3znYx16boQ8oDql9SGU0swAl70NtRgA9GTTnz"}
    url_epic = "https://api.nasa.gov/EPIC/api/enhanced/images"
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


def fetch_spacex_last_launch():
    id = "5eb87d47ffd86e000604b38a"
    url_SpaceX = f'https://api.spacexdata.com/v5/launches/{id}'
    response_SpaceX = requests.get(url_SpaceX)
    SpaceX_links = response_SpaceX.json()["links"]
    SpaceX_photos = SpaceX_links["flickr"]["original"]
    for image_number, SpaceX_photo_url in enumerate(SpaceX_photos):
        filename = f'SpaceX_photo_{image_number}.jpeg'
        download_photo(filename, SpaceX_photo_url)


pictory_day_nasa()
pictory_epic()
fetch_spacex_last_launch()