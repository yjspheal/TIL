# 4615. 재미있는 오셀로 게임

import sys

sys.stdin = open('sample_input(1).txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxN, M = 돌 놓는 횟수

    black_count = 2
    white_count = 2

    for _ in range(M):
        r, c, color = map(int, input().split())

        if color == 1:  # 흑돌
            black_count += 2
            white_count -= 1
        else:
            black_count -= 1
            white_count += 2

    print(f'#{tc} {black_count} {white_count}')
