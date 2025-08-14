- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 위험 좌표를 set으로 수집](#1-위험-좌표를-set으로-수집)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 경비병

"""
0 - 빈칸, 1 - 벽, 2 - 경비병
경비병은 상하좌우로 관찰하며, 벽에 막하지 않는 곳까지 시야가 뻗어나간다.
안전한 빈 칸의 수를 구하라.
"""

import sys
sys.stdin = open('input.txt')

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
    ym_arr = [list(input().split()) for _ in range(N)]  # 멀캠 정보가 들어있는 이차원배열

    empty_areas = 0  # 빈 칸 수
    warning_empty_areas = 0  # 위험 칸 수

    # 멀캠 정보를 순회하며
    for row in range(N):
        for col in range(N):
            if ym_arr[row][col] == '0':  # 빈칸이라면
                empty_areas += 1
            elif ym_arr[row][col] == '2':  # 경비병이라면
                # 위험한 칸 계산
                warning_empty_areas = count_warning_areas(ym_arr, N, row, col)

    print(f'#{tc} {empty_areas - warning_empty_areas}')
~~~
<br><br>


# 총평
- 경비병 위치에서 4방향으로 벽(1) 전까지의 빈 칸 수를 계산하는 기본 로직은 맞습니다.
- 입력 값이 `'0'` 문자열이므로, int 변환 없이 문자열 비교가 일관성 있게 처리되었습니다.
- `count_warning_areas`는 빈 칸 수를 세는 것이 아니라 **위험 좌표**를 반환하게 변경하면 중복 제거가 쉬워집니다.
<br><br>


# 보완점
## 1. 위험 좌표를 set으로 수집
- 각 경비병의 시야를 set에 추가하면 자동으로 중복이 제거됩니다.
- 최종적으로 `safe_count = empty_areas - len(warning_positions)`로 계산 가능.
~~~python
def guard_view_positions(arr, n, r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    positions = set()
    for i in range(4):
        k = 1
        while True:
            nr = r + dr[i] * k
            nc = c + dc[i] * k
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == '0':
                positions.add((nr, nc))
                k += 1
            else:
                break
    return positions
~~~


<br><br>


# 최종 코드 예시
~~~python
# 경비병 - 안전한 빈 칸 계산

from typing import List, Set, Tuple

def guard_view_positions(arr: List[List[str]], n: int, r: int, c: int) -> Set[Tuple[int, int]]:
    """경비병 위치(r,c)에서 4방향으로 벽(1) 전까지의 빈 칸 좌표 집합 반환"""
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    positions = set()
    for i in range(4):
        k = 1
        while True:
            nr = r + dr[i] * k
            nc = c + dc[i] * k
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == '0':
                positions.add((nr, nc))
                k += 1
            else:
                break
    return positions

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        grid = [input().split() for _ in range(N)]
        empty_count = 0
        warning_positions: Set[Tuple[int, int]] = set()

        for r in range(N):
            for c in range(N):
                if grid[r][c] == '0':
                    empty_count += 1
                elif grid[r][c] == '2':
                    warning_positions |= guard_view_positions(grid, N, r, c)

        safe_count = empty_count - len(warning_positions)
        print(f'#{tc} {safe_count}')

if __name__ == "__main__":
    main()
~~~
- 이렇게 하면 경비병이 여러 명 있어도 중복 위험 구역은 한 번만 카운트됩니다.
- 시간복잡도는 O(N²)로 동일하며, 공간은 최대 빈칸 수만큼 set을 사용합니다.
