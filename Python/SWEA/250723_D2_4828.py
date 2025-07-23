# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    nums = list(map(int,input().split())) # 숫자 리스트 생성
    
    mini = min(nums)
    maxi = max(nums)
    print(f'#{test_case} {maxi - mini}')