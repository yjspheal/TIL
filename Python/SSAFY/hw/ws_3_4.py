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


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 방법 1(with map)

every_user_infos = []
for user_info in map(lambda x, y, z: (x,y,z), name, age, address):
    every_user_infos.append(create_user(*user_info))
    
print(every_user_infos)

# # 방법 2(with zip)

# every_user_infos = []
# for user_info in zip(name, age, address):
#     every_user_infos.append(create_user(*item))

# print(every_user_infos)



