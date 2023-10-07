import requests
import os


def download_photo(foldername, filename, url):
    if not os.path.isdir(foldername):
        os.mkdir(foldername)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)

foldername = 'images'


def fetch_spacex_last_launch():
    id = "5eb87d47ffd86e000604b38a"
    url_SpaceX = f'https://api.spacexdata.com/v5/launches/{id}'
    response_SpaceX = requests.get(url_SpaceX)
    SpaceX_links = response_SpaceX.json()["links"]
    SpaceX_photos = SpaceX_links["flickr"]["original"]
    for image_number, SpaceX_photo_url in enumerate(SpaceX_photos):
        filename = f'{foldername}/SpaceX_photo_{image_number}.jpeg'
        download_photo(foldername, filename, SpaceX_photo_url)



fetch_spacex_last_launch()