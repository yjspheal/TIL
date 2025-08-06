import sys
from pprint import pprint

sys.stdin = open('input.txt')

# 테케 갯수 입력
T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, T + 1):
    _ = int(input())    # 5로 고정
    # 공백으로 구분된 5X5 배열
    arr = [list(map(int, input().split())) for _ in range(5)]

    # 행, 열 길이 저장
    N = len(arr)
    M = len(arr[0])

    # 모든 위치에서의 상하좌우 sum 구하기 위한 변수 초기화
    result = 0

    # 행을 순회하며
    for r in range(N):
        # 열을 순회하며
        for c in range(M):
            # dr, dc를 순회하며
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 인접한 요소가 벽이 아닐 때만 합을 더함
                if 0 <= nr < N and 0 <= nc < N:
                    result += abs(arr[nr][nc] - arr[r][c])

    print(f"#{tc} {result}")