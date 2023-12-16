import requests
import argparse

from Download_images import download_photo


def fetch_spacex_last_launch(id):
    url_spacex = f'https://api.spacexdata.com/v5/launches/{id}'
    response_spacex = requests.get(url_spacex)
    spacex_links = response_spacex.json()["links"]
    spacex_photos = spacex_links["flickr"]["original"]
    for image_number, spacex_photo_url in enumerate(spacex_photos):
        filename = f'SpaceX_photo_{image_number}.jpeg'
        download_photo(filename, spacex_photo_url)


def main():

    parser = argparse.ArgumentParser(
        description='получение фото запусков'
    )
    parser.add_argument('--id', help='id нужного вам запуска', default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()

    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()