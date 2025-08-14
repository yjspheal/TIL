- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 레이저 진행/정지 조건 명확화](#1-레이저-진행정지-조건-명확화)
  - [2. 괴물 위치 1회 탐색 후 즉시 계산](#2-괴물-위치-1회-탐색-후-즉시-계산)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 23795. 우주괴물

# import sys
# sys.stdin = open('sample_in.txt')

"""
0 - 빈칸, 1 - 벽, 2 - 괴물
괴물은 상하좌우로 광선을 발사하며, 벽에 막하지 않는 곳까지 뻗어나간다.
안전한 빈 칸의 수를 구하라.
"""


def count_warning_areas(arr, len_arr, r, c):
    """
    행 열 길이가 len_arr인 이차원배열 arr에 대해, arr[row][col]를 기준으로
    상하좌우에서 벽(1)에 막히기 전까지의 빈 칸(0)의 수를 구하여 retur
    """

    warning_counts = 0  # 위험한 칸의 수

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]  # 행 열 델타 정의

    for i in range(4):
        k = 1
        while True:
            nr = r + dr[i] * k  # 새로운 r
            nc = c + dc[i] * k  # 새로운 c

            if 0 <= nr < len_arr and 0 <= nc < len_arr and arr[nr][nc] == '0':  # 범위에 있고 빈 칸이라면
                warning_counts += 1  # count + 1
                k += 1  # 다음 칸으로
            else:
                break

    return warning_counts


T = int(input())  # 테케 수
for tc in range(1, T + 1):
    N = int(input())  # NxN
    space = [list(input().split()) for _ in range(N)]  # 우주 정보가 들어있는 이차원배열

    empty_areas = 0  # 빈 칸 수
    warning_empty_areas = 0  # 위험 칸 수(없어도 되지만 밑에 밑줄그어지지말라고..)

    # space를 순회하며
    for row in range(N):
        for col in range(N):
            if space[row][col] == '0':  # 빈칸이라면
                empty_areas += 1
            elif space[row][col] == '2':  # 괴물이라면
                # 위험한 칸 계산
                warning_empty_areas = count_warning_areas(space, N, row, col)

    print(f'#{tc} {empty_areas - warning_empty_areas}')
~~~
<br><br>


# 총평
- 괴물은 **1개 보장**이므로 “전체 빈칸 수 − 해당 괴물이 비추는 빈칸 수” 한 번만 계산하면 됩니다.
- 레이저는 **벽(1)에서만 멈춤**: 기존 함수는 `'0'`이 아닐 때 바로 중단해 불필요하게 보수적입니다.
- `len_arr` 인자는 불필요하며, `len(arr)`로 대체하면 함수가 단순해집니다.
<br><br>


# 보완점
## 1. 레이저 진행/정지 조건 명확화
- 진행: 경계 내이면서 **벽이 아닐 때** 계속 전진
- 카운트: **빈칸(0)** 만 카운트
- 정지: **벽(1)** 만나면 즉시 정지

~~~python
while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != '1':
    if grid[nr][nc] == '0':
        danger += 1
    k += 1
~~~

<br><br>


## 2. 괴물 위치 1회 탐색 후 즉시 계산
- 전체 빈칸 수(`total_zero`)와 괴물 좌표(`mr, mc`)만 먼저 수집하고
- 한 번만 `count_warning_areas` 실행

<br><br>


# 최종 코드 예시
~~~python
# 23795. 우주괴물
# 조건: 괴물(2)은 정확히 하나

import sys
# sys.stdin = open('sample_in.txt')

def count_warning_areas(grid, r, c):
    """
    (r, c)에 위치한 단 하나의 괴물에서 상/하/좌/우로 레이저를 쏘아,
    벽(1)에 막히기 전까지 만나는 빈칸(0)의 개수를 반환한다.
    """
    N = len(grid)
    danger = 0
    dr = (-1, 1, 0, 0)
    dc = (0, 0, 1, -1)

    for d in range(4):
        k = 1
        while True:
            nr = r + dr[d] * k
            nc = c + dc[d] * k
            if not (0 <= nr < N and 0 <= nc < N):
                break
            if grid[nr][nc] == '1':  # 벽에서 정지
                break
            if grid[nr][nc] == '0':  # 빈칸은 위험
                danger += 1
            # grid[nr][nc] == '2'는 통과 (괴물은 1개이므로 재조우 없음)
            k += 1
    return danger

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        # 입력 형식에 맞게 한 줄을 그대로 문자 리스트로 읽음 (예: 01020)
        grid = [list(input().strip()) for _ in range(N)]

        total_zero = 0
        mr = mc = -1

        for r in range(N):
            for c in range(N):
                v = grid[r][c]
                if v == '0':
                    total_zero += 1
                elif v == '2':
                    mr, mc = r, c

        # 괴물은 하나 보장
        danger = count_warning_areas(grid, mr, mc)
        safe = total_zero - danger
        print(f"#{tc} {safe}")

if __name__ == "__main__":
    solve()
~~~
