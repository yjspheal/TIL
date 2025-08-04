# 아래 클래스를 수정하시오.
class StringRepeater:
    """
    주어진 문자열을 반복 출력하는 클래스
    """
    def __init__(self):
        pass

    def repeat_string(self, count, message):
        """
        반복 횟수와 문자열을 인자로받아 문자열을 반복 출력하는 메서드
        """
        for time in range(count):
            print(message)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
