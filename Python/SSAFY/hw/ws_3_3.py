def rental_book(name, number):
    decrease_book(number)

    print(f'{name}님이 {number}권의 책을 대여하셨습니다.')
    pass

number_of_book = 100

def decrease_book(n):
    global number_of_book
    number_of_book -= n

    print(f'남은 책의 수 : {number_of_book}')
    pass


rental_book('홍길동', 3)