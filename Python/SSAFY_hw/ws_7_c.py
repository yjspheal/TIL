class Car:
    # 아래에 코드를 작성하시오.
    pass

    # 모든 차가 공통으로 가질 클래스 변수
    wheels = 4

    def __init__(self, engine, driving_system, sound):
        self.engine = engine        # 엔진 종류
        self.driving_system = driving_system        # 구동 방식
        self.sound = sound          # 엔진 소리
    
    # 인스턴스 메서드
    def drive(self):
        """
        인스턴스가 가진 고유 사운드를 출력하고 engine을 반환한다
        """
        print(self.sound)

        return self.engine
    
    def introduce(self):
        """
        인스턴스의 엔진 종류, 구동 방식을 소개하는 문자열을 출력한다.
        """

        print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')

    @classmethod
    def increase_wheels(cls):
        """
        호출 될 때마다 클래스 변수 wheels가 1 증가
        안내 문자열 출력
        """

        cls.wheels += 1
        print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1증가하였습니다.')


    @staticmethod
    def description():
        """
        '자동차'에 대한 설명을 출력하는 함수
        """

        print('자동차(自動車, 영어: car, automobile)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.')



car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
print(car2.drive())

print('===')
car1.introduce()
car3.introduce()

print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.description()