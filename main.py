import sys

import requests

from settings import TOKEN


class YaUploader:

    URL = 'https://cloud-api.yandex.net'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str) -> None:
        
        headers = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(f'{self.URL}/v1/disk/resources/upload', headers=headers, params={'path': file_path})
        data = response.json()
        if response.status_code != requests.codes.ok:
            print(data)
            return
        requests.put(data['href'], headers=headers, files={'file': open(file_path, 'rb')})


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)