# 12712_파리퇴치3. 파리퇴치3

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기 변수들 설정
    fly_matrix = []
    max_fly = 0

    # 파리 matrix 완성
    for time in range(N):
        fly_matrix.append(list(map(int, input().split())))  # 리스트로 변환

    # 중심을 기준으로 M-1씩 분사됨
    for center in range(N**2):
        c_row = center // N
        c_col = center % N  # ← 여기 % 5 → % N 으로 수정

        # 잡은 파리 수 초기화
        plus_catch = fly_matrix[c_row][c_col]
        cross_catch = fly_matrix[c_row][c_col]

        # + 모양 처리 (상, 하, 좌, 우)
        for i in range(1, M):
            if c_row - i >= 0:
                plus_catch += fly_matrix[c_row - i][c_col]
            if c_row + i < N:
                plus_catch += fly_matrix[c_row + i][c_col]
            if c_col - i >= 0:
                plus_catch += fly_matrix[c_row][c_col - i]
            if c_col + i < N:
                plus_catch += fly_matrix[c_row][c_col + i]

        # x 모양 처리 (대각선)
        for i in range(1, M):
            if c_row - i >= 0 and c_col - i >= 0:
                cross_catch += fly_matrix[c_row - i][c_col - i]
            if c_row - i >= 0 and c_col + i < N:
                cross_catch += fly_matrix[c_row - i][c_col + i]
            if c_row + i < N and c_col - i >= 0:
                cross_catch += fly_matrix[c_row + i][c_col - i]
            if c_row + i < N and c_col + i < N:
                cross_catch += fly_matrix[c_row + i][c_col + i]

        max_fly = max(max_fly, plus_catch, cross_catch)

    print(f"#{test_case} {max_fly}")
