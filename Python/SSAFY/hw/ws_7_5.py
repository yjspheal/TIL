# 아래 클래스를 수정하시오.
class Shape:
    pass
    # 가로와 세로 길이를 인자로 받아 속성으로 저장한다.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # # 메서드를 추가하여 사각형의 넓이를 계산하여 반환하시오
    # def calculate_area(self):
    #     return self.width * self.height
    
    # # 사각형의 둘레를 계산하는 메서드
    # def calculate_perimeter(self):
    #     return 2 * (self.width + self.height)

    # # 사각형의 가로, 세로, 넓이, 둘레를 출력하는 메서드 추가
    # def print_info(self):
    #     print(f'Width: {self.width}')
    #     print(f'Height: {self.height}')
    #     print(f'Area: {self.calculate_area()}')
    #     print(f'Perimeter: {self.calculate_perimeter()}')

    # __str__매직 메서드를 추가하여 인스턴스를 문자열로 표현할 수 있도록 코드를 작성하시오
    def __str__(self):
        return f"Shape: width={self.width}, height={self.height}"
    

shape1 = Shape(5, 3)
print(shape1)
