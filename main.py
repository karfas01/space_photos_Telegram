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
filename = f'{foldername}/dvmn.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"



download_photo(foldername, filename, url)