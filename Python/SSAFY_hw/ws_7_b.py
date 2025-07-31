# 아래에 코드를 작성하시오.
class Myth:
    # 인스턴수 수 기록 변수
    type_of_myth = 0

    # 생성자 메서드 정의
    # 신화의 이름을 인자로 받는다
    def __init__(self, name):
        self.name = name

        # 인스턴스 생성 시 type_of_myth가 증가하도록
        Myth.increase_myth()

    # type_of_myth가 1 증가한다
    @classmethod
    def increase_myth(cls):
        cls.type_of_myth += 1

    # myth를 설명하는 description용 staticmethod 생성
    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

    

dangun = Myth('dangun')     # 단군 인스턴스 생성
greek_rome = Myth('greek & rome')     # 그리스로마신화 인스턴스 생성

# 각 인스턴스의 name 출력
print(dangun.name)
print(greek_rome.name)

print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description()