number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1



def create_user(name, age, address):
    increase_user()


    user_info = {}

    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address


    print(f'{user_info["name"]}님 환영합니다!')

    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')

user_gildong = create_user('홍길동', 30, '서울')       # 호출

print(user_gildong)     # 호출된 결과 출력

print(f'현재 가입 된 유저 수 : {number_of_people}')
