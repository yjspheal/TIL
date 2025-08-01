# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")

"""
IDEA
- NxN행렬에서 행 열 안 겹치게 pick할 수 있는 경우를 모두 구한다
- 즉 경우의 수는 N!
- 해당 경우를 모두 돌면서, min_sum값을 넘어서는 순간 break한다
- 2초 안 넘지 않을까?
- 넘네...어카지?
"""

# 구글링해서 찾았음!!
import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())# NxN 행렬의 N을 input
    
    # 숫자를 싹 순서대로 담은 arr
    arr = []
    for _ in range(N):
        # 들어오는 숫자 리스트를 하여 arr에 추가
        nums = tuple(map(int, input().split()))

        arr.append(nums)

    """
    한줄로 받았으므로, 선택할 수 있는 인덱스는 다음과 같다
    한 줄의 i
    다음 줄의 j(i가 아닌)
    그 다음 줄의 k(i, j가 아닌)

    그렇다면?
    i, j, k ...는 0 ~ N-1

    즉 0부터 N-1까지 싹 순열시키면 됨

    순열시키는 모듈이 있음
    """
    # 012345..N-1 문자열 만들기
    N_list = ''.join([str(_) for _ in range(N)])
    # 순열하기
    lineups = map(''.join, itertools.permutations(N_list))
    
    # 최저합 ㅊ초기화
    min_sum = 10000

    # 순열 결과가 하나씩 나옴
    for lineup in lineups:
        current_sum = 0
        # i번쨰 줄에서 택할 것들을 하나씩 더함
        for i in range(N):
            current_num = arr[i][int(lineup[i])]
            current_sum += current_num

            # 만약 이번 라인업에서 최저 sum을 이미 넘겨버렸다면 다음으로
            if current_sum > min_sum:
                break

        if current_sum < min_sum:
            min_sum = current_sum


    print(f'#{tc} {min_sum}')