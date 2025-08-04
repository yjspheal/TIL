number_of_book = 100


def decrease_book(n):
    '''
    현재 잔여 책 수에서 n을 빼어 남은 책의 수를 print하는 함수
    '''
    global number_of_book
    number_of_book -= n

    print(f'남은 책의 수 : {number_of_book}')
    pass


def create_user(name, age, address):
    '''
    name, age, address를 인자로 받아, 환영 인사 print 후, 하나의 딕셔너리로 return하는 함수
    '''

    user_info = {}

    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address


    print(f'{user_info["name"]}님 환영합니다!')

    return user_info
    


def rental_book(info):
    '''
    신규 고객 정보를 담은 딕셔너리 info를 인자로 받아
    decrease_book함수로 잔여 책 수를 refresh 후
    누가 몇권을 대여했는지 print하는 함수
    '''
    rental_count = info['age'] // 10
    decrease_book(rental_count)

    print(f'{info["name"]}님이 {rental_count}권의 책을 대여하셨습니다.')

    pass



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


many_user = []
for user_info in map(lambda x, y, z: (x,y,z), name, age, address):
    many_user.append(create_user(*user_info))

# print(many_user)


user_dicts = map(lambda x: {'name': x['name'],'age': x['age']}, many_user)
# print(user_dicts)

list(map(rental_book,user_dicts))