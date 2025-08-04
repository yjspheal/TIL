# 아래 클래스를 수정하시오.
class Shape:
    pass
    # 가로와 세로 길이를 인자로 받아 속성으로 저장한다.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 메서드를 추가하여 사각형의 넓이를 계산하여 반환하시오
    def calculate_area(self):
        return self.width * self.height


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
