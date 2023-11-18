import requests

from Download_images import download_photo


def fetch_spacex_last_launch():
    id = "5eb87d47ffd86e000604b38a"
    url_SpaceX = f'https://api.spacexdata.com/v5/launches/{id}'
    response_SpaceX = requests.get(url_SpaceX)
    SpaceX_links = response_SpaceX.json()["links"]
    SpaceX_photos = SpaceX_links["flickr"]["original"]
    for image_number, SpaceX_photo_url in enumerate(SpaceX_photos):
        filename = f'SpaceX_photo_{image_number}.jpeg'
        download_photo(filename, SpaceX_photo_url)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()