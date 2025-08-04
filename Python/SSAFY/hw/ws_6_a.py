my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
# my set을 순회하며 얻은 값을 key로 하는 my_dict의 value를 출력한다
# key가 없으면 None이 출력되도록 한다.
for key in my_set:
    print(my_dict.get(key))

# var 변수에 dict의 키로 사용 가능한 자료형을 할당한다.
var = 'spheal'
my_dict[var] = '변수로도 키 설정 가능'

print(my_dict)

