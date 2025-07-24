import requests
# from pprint import pprint as print

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


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}

    for user in user_list:
        company_name = user['company']
        username = user['name']

        if censorship(company_name, username):
            # print(company_name)
            censored_user_list[company_name] = [username]
        
    # print(censored_user_list)
    return censored_user_list


def censorship(company, name):
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print(f'이상 없습니다.')
        return True

print(create_user(dummy_data))