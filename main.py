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


url_SpaceX = 'https://api.spacexdata.com/v5/launches/latest'
response_SpaceX = requests.get(url_SpaceX)
print(response_SpaceX.json())


download_photo(foldername, filename, url)
