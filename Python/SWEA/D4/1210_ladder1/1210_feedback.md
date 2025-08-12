- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 수평-수직 규칙으로 단순화 (플래그 제거)](#1-수평-수직-규칙으로-단순화-플래그-제거)
  - [2. 불필요한 복잡 조건 제거 및 경계 처리 명확화](#2-불필요한-복잡-조건-제거-및-경계-처리-명확화)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

"""
idea
1. 도착지에서 시작해서 거슬러 올라간다.
2. 좌 or 우를 만난다면 막힐 때까지, 즉 1인동안 해당 방향으로 계속 이동
3. 막히면, 좌우를 만날 때까지 올라간다.
4. 행이 0이되면 해당 col값을 출력

[제약 사항]
한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
"""


# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# # sys.stdin = open("sample_input.txt", "r")
# sys.stdin = open("input.txt", "r")

def climb_ladder(arr, end_c):
    """
    0(벽), 1(길), 2(도착점)로 이루어진 이차원 리스트 arr에 대해서, 1만을 이어서 2에 도달하게 되는 루트의 시작점의 col값을 반환
    단, 경로는 위에서 아래로만 진행되어야 함

    Args:
        arr (list): 0, 1, 2로 이루어진 이차원 리스트
        end_c (int): 도착점의 열 값

    Returns:
        int: 시작점의 col 값
    """
    N = 100     # 총 행 수

    r = N - 1      # 현재는 마지막줄이므로 99에 위치
    c = end_c   # 현재 col 위치

    # 방금까지 왼쪽으로 왔으면 오른쪽에 길이 있는 것이 당연
    # 그렇게 가면 무한으로 도므로 방지용 변수 제작
    going_right = False
    going_left = False

    while r > 0:    # 행이 0이 되면 끝
        # 왼쪽에 길이 있다면
        if 0 <= c - 1 < N and arr[r][c - 1] == 1 and not going_right:
            # 끝까지 간다
            while True:
                going_left = True
                c -= 1
                if c == 0 or arr[r][c-1] == 0:      # 열이 0, 즉 왼쪽 끝에 도달했거나 벽에 막히게되면 break
                    r -= 1 if r > 0 else 0     # 첫줄이 아니라면 1 올라간다
                    break

        # 오른쪽에 길이 있다면
        # print(r, c)
        if 0 <= c + 1 < N and arr[r][c + 1] == 1 and not going_left:
            # 끝까지 간다
            while True:
                going_right = True
                c += 1
                if c == 99 or arr[r][c+1] == 0:      # 열이 99, 즉 오른쪽 끝에 도달했거나 벽에 막히게되면 break
                    r -= 1 if r > 0 else 0     # 첫줄이 아니라면 1 올라간다
                    break

        # 좌우가 막혔다면 위로 올라감. 다만 이번엔 막힐 때까지가 아닌, 다음 좌우가 나올 때까지.
        while (r > 0) and (c == 0 and arr[r][c+1] == 0) or (c == 99 and arr[r][c-1] == 0) or (1 <= c < N and arr[r][c-1] == 0 and arr[r][c+1] == 0):
        # 너무 긴데...?
            going_left = going_right = False    # 로 초기화
            r -= 1
            if r == 0:  # 첫 행에 도달했다면 break
                break

    # 현재 c가 출발 c가 된다.
    return c

T = 10  # 테케 10으로 고정
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    _ = int(input())  # 테케 번호와 동일
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 사다리 정보 담긴 이차원 배열

    # 도착점 찾기
    end_col = 0
    for c in range(100):
        if ladder[-1][c] == 2:      # 2는 항상 마지막줄에있으므로
            end_col = c

    # 첫 col값 찾기
    start_col = climb_ladder(ladder, end_col)

    print(f'#{tc} {start_col}')
~~~
<br><br>


# 총평
- 핵심 아이디어(좌/우가 보이면 막힐 때까지 수평 이동, 아니면 위로 이동)는 정확합니다.
- 다만 방향 플래그(`going_left`, `going_right`)와 복잡한 조건식으로 인해 가독성과 안정성이 떨어집니다.
- 특히 `while`문의 긴 논리식은 **연산자 우선순위** 때문에 의도치 않은 평가가 발생할 위험이 큽니다.
- 이 문제는 “항상 수평을 끝까지 간 뒤 한 칸 위로 올라가고, 다시 좌/우를 먼저 본다”는 단순한 규칙으로 깔끔하게 구현 가능합니다(플래그 불필요).
- 입력 처리에서 도착 열을 찾을 때 `break`가 없어 미세하게 비효율적입니다.

<br><br>


# 보완점
## 1. 수평-수직 규칙으로 단순화 (플래그 제거)
좌/우 중 하나가 1이면 해당 방향으로 **연속 이동**만 하고, 끝나면 **위로 한 칸** 올라가는 패턴으로 충분합니다. 위로 올라간 후 다시 좌/우를 우선 확인하면 자연스럽게 다음 수평 구간으로 진입합니다.
~~~python
def climb_ladder(arr, end_c):
    N = 100
    r, c = N - 1, end_c
    while r > 0:
        # 왼쪽이 길이면 왼쪽으로 끝까지
        if c > 0 and arr[r][c-1] == 1:
            while c > 0 and arr[r][c-1] == 1:
                c -= 1
            r -= 1
            continue
        # 오른쪽이 길이면 오른쪽으로 끝까지
        if c < N-1 and arr[r][c+1] == 1:
            while c < N-1 and arr[r][c+1] == 1:
                c += 1
            r -= 1
            continue
        # 좌/우가 모두 막혀 있으면 위로
        r -= 1
    return c
~~~

<br><br>


## 2. 불필요한 복잡 조건 제거 및 경계 처리 명확화
기존의
~~~python
while (r > 0) and (c == 0 and arr[r][c+1] == 0) or ...
~~~
는 괄호가 부족해 의도와 다르게 평가될 수 있습니다. 위의 개선안처럼 **세 단계(좌, 우, 위)**로 분기하면 이 긴 조건 자체가 필요 없어집니다.

<br><br>


# 최종 코드 예시
~~~python
# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# 규칙: 좌/우가 보이면 해당 방향으로 끝까지 → 위로 한 칸 → 반복

import sys

def climb_ladder(arr, end_c):
    N = 100
    r, c = N - 1, end_c
    while r > 0:
        # 왼쪽 길이 있으면 끝까지 이동
        if c > 0 and arr[r][c-1] == 1:
            while c > 0 and arr[r][c-1] == 1:
                c -= 1
            r -= 1
            continue
        # 오른쪽 길이 있으면 끝까지 이동
        if c < N - 1 and arr[r][c+1] == 1:
            while c < N - 1 and arr[r][c+1] == 1:
                c += 1
            r -= 1
            continue
        # 수평 길이 없으면 위로
        r -= 1
    return c

def main():
    input = sys.stdin.readline
    T = 10  # 고정
    for tc in range(1, T + 1):
        _ = int(input())  # 테스트케이스 번호(사용 안 함)
        ladder = [list(map(int, input().split())) for _ in range(100)]

        # 도착 열 찾기 (마지막 행에서 값 2)
        last_row = ladder[-1]
        end_col = next(i for i, v in enumerate(last_row) if v == 2)

        start_col = climb_ladder(ladder, end_col)
        print(f"#{tc} {start_col}")

if __name__ == "__main__":
    # 온라인 저지에서는 stdin 리다이렉트 금지
    # sys.stdin = open("input.txt", "r")
    main()
~~~
