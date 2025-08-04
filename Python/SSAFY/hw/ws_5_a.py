N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.

# data_1 문자열을 돌며 하나씩 arr_1에 append
for digit in data_1:
    arr_1.append(digit)
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

# data_2를 공백 기준으로 split한 다음 int화
arr_2 = list(map(int, data_2.split()))

for digit in arr_2:
    # 홀수만 출력
    if digit % 2 == 1:
        print(digit)