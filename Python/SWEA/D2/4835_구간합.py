# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합


'''
[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )

다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )
'''

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _, M = map(int, input().split())

    digit_list = list(map(int, input().split()))
    min_sum = 100 * 100 * 10000     # 초기값: 문제에서 주어진 sum값의 최대
    max_sum = 0                     # 초기값: sum값 최저


    for i in range(len(digit_list) - M + 1): # 마지막에서 M번째까지의 숫자를 선택해야하므로
        current_sum = sum(digit_list[i:(i+M)])  # index i부터 i+M-1 까지 총 M개의 숫자를 더함

        if current_sum > max_sum:       # current가 max_sum을 넘겼다면
            max_sum = current_sum
        if current_sum < min_sum:       # current가 min_sum보다 작다면
            min_sum = current_sum


    
    print(f'#{test_case} {max_sum - min_sum}')


