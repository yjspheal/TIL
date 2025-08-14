- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 센티넬 기법으로 마지막 원소 처리 단순화](#1-센티넬-기법으로-마지막-원소-처리-단순화)
  - [2. 가로/세로 합치기보다 별도 함수 2회 호출](#2-가로세로-합치기보다-별도-함수-2회-호출)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 20739. 고대 유적 2

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 이중리스트로 input받음
    arr += list(map(list, zip(*arr)))  # 세로줄을 가로로 transpose하여 arr에 추가

    max_length = 0  # 가장 긴 구조물의 길이를 넣을 변수

    # arr를 순회하며
    for row in arr:
        current_length = 0  # 현재 길이 변수
        len_row = len(row)
        for i, ele in enumerate(row):  # row의 각 원소에 대해
            if ele == 1:  # 구조물이면 현재 길이 +1
                current_length += 1
                if i < len_row - 1:   # 마지막 원소가 아니라면
                    continue    # 다음 턴으로

            # 마지막 원소거나, 구조물이 아닐 때 아래 if를 돌림
            if current_length > max_length:  # 현재 길이가 최대 길이를 넘었다면 update
                max_length = current_length

            current_length = 0  # 현재 길이 초기화

    # 젤 긴 게 1이면 노이즈라는 뜻이므로 0 출력
    if max_length == 1:
        max_length = 0

    print(f'#{tc} {max_length}')
~~~
<br><br>


# 총평
- 가로/세로를 모두 `arr`에 합쳐 한 번의 루프에서 최댓길이를 찾는 접근이 깔끔합니다.
- 행 내부에서 `1`이 연속되는 구간 길이를 카운트하고, 마지막 원소 처리도 잘 되어 있습니다.
- 다만 **`if i < len_row - 1: continue`** 구문 때문에, 마지막 원소가 `1`일 때만 구간 종료를 처리하는 흐름이 약간 우회적입니다.  
  → **센티넬(0을 끝에 추가)** 기법을 쓰면 더 단순화할 수 있습니다.
- 현재는 `max_length == 1`이면 `0`으로 바꾸는 후처리를 하고 있는데, 계산 중에 `max_length`를 갱신할 때 바로 필터링하는 것도 가능.
- 하드코딩 없이 가독성을 높이려면 **함수화** + **타입 힌트**를 추천합니다.
<br><br>


# 보완점
## 1. 센티넬 기법으로 마지막 원소 처리 단순화
- 각 행 끝에 `0`을 덧붙이면, 마지막 원소가 `1`이든 `0`이든 동일한 방식으로 구간 종료를 처리할 수 있습니다.
~~~python
for row in arr:
    cnt = 0
    for v in row + [0]:  # 끝에 0 추가
        if v == 1:
            cnt += 1
        else:
            if cnt > max_length:
                max_length = cnt
            cnt = 0
~~~

<br><br>


## 2. 가로/세로 합치기보다 별도 함수 2회 호출
- 전치로 세로줄을 만드는 건 동일하지만, 원본과 전치 모두를 같은 함수에 돌리면 메모리 절약 + 의도 명확.
~~~python
def max_consecutive_ones(lines):
    max_len = 0
    for row in lines:
        cnt = 0
        for v in row + [0]:
            if v == 1:
                cnt += 1
            else:
                if cnt > max_len:
                    max_len = cnt
                cnt = 0
    return max_len
~~~

<br><br>


# 최종 코드 예시
~~~python
# 20739. 고대 유적 2

from typing import List

def max_consecutive_ones(lines: List[List[int]]) -> int:
    """2차원 리스트에서 연속된 1의 최대 길이 반환"""
    max_len = 0
    for row in lines:
        cnt = 0
        for v in row + [0]:  # 센티넬
            if v == 1:
                cnt += 1
            else:
                if cnt > max_len:
                    max_len = cnt
                cnt = 0
    return max_len

def solve_case() -> int:
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    horizontal_max = max_consecutive_ones(grid)
    vertical_max = max_consecutive_ones([list(col) for col in zip(*grid)])
    max_length = max(horizontal_max, vertical_max)
    # 길이가 1이면 노이즈 처리
    return 0 if max_length == 1 else max_length

def main():
    T = int(input())
    for tc in range(1, T + 1):
        ans = solve_case()
        print(f'#{tc} {ans}')

if __name__ == "__main__":
    main()
~~~
