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