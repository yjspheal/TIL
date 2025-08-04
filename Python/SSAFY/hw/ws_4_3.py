
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'


dummy_data = []
# 1 ~ 10까지 API 요청
for i in range(1, 11):
    response = requests.get(API_URL + f'{i}')
    

    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # print(parsed_data)

    name = {}

    name['name'] = parsed_data['name']
    name['lat'] = parsed_data['address']['geo']['lat']
    name['lng'] = parsed_data['address']['geo']['lng']
    name['company'] = parsed_data['company']['name']

    lat = float(name['lat'])
    lng = float(name['lng'])

    if (lat < 80 and lat > -80) and (lng < 80 and lng > -80):
        dummy_data.append(name)

print(dummy_data)