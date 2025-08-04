# 아래 클래스를 수정하시오.
class Person:
    pass

    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 인원 1명 추가
        Person.add_number_people()

    # 소개함수
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
    
    @classmethod
    def add_number_people(cls):
        cls.number_of_people += 1


person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
