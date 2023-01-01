import requests


URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"


def main(superheroes= ['Hulk', 'Captain America', 'Thanos']):
    response = requests.get(URL)
    data = {}
    for h in response.json():
        if h['name'] in superheroes:
            data[h['name']] = h['powerstats']['intelligence']
    for k, v in sorted(data.items(), key= lambda x: x[1], reverse=True):
        print(k, v)


main()