data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

for char in data_1:
    # 대문자거나 공백만 출력, 한줄에
    if char.isupper() or char == ' ':
        print(char, end = '')



print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

# 내힘들다 index 찾아 arr에 append
arr.append(data_2.index('내'))
arr.append(data_2.index('힘'))
arr.append(data_2.index('들'))
arr.append(data_2.index('다'))

# arr 출력
print(arr)

# arr 정렬 후 출력
arr.sort()
print(arr)

# data_2에서 해당 인덱스 찾아 한줄로 출력
for index in arr:
    print(data_2[index], end = '')