- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. `current_mok` 제거 및 반복 인덱스 기반 판정](#1-current_mok-제거-및-반복-인덱스-기반-판정)
  - [2. 전역 의존 제거](#2-전역-의존-제거)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 11315_오목판정. 오목 판정
"""
idea
첫줄부터 돌면서, 돌을 만나면  우 우하 하 좌하 네 방향을 탐색하며 오목여부를 계산한다
"""
# import sys
#
# sys.stdin = open('sample_input.txt')


def check_omok(arr):
    """
    arr를 돌며, 가로 세로 대각선 방향으로 O가 연속 다섯 개 있는지 여부를 판단하여 return
    Args:
        arr(list): .과 O로 이루어진 이차원 리스트
    Returns:
        str: 다섯개 있다면 YES, 없다면 NO를 반환
    """
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]  # 우 우하 하 좌하 델타

    n = N  # 바둑판 한줄 길이

    # 바둑판을 돌며
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'o':  # 돌이면
                current_mok = 1  # 현재 연속 돌에 1 할당

                for i in range(4):  # 네가지 방향 탐색
                    for k in range(1, 5):   # 현재 다음부터 4개까지만 연속인지 보면 됨
                        nr = r + dr[i] * k
                        nc = c + dc[i] * k

                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':      # 바둑판 안에 있고 또 돌이면
                            current_mok += 1    # 목 + 1

                        else:
                            break   # 아닌 순간 바로 break하여 다음 방향 탐색

                    else:   # 다섯개를 다 봤는데 break가 안 됐다면 오목
                        return 'YES'

    # 리턴이 한번도 안 됐다면, 즉 오목이 없다는 것
    else:
        return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    baduk = [list(input()) for _ in range(N)]

    result = check_omok(baduk)
    print(f'#{tc} {result}')
~~~
<br><br>


# 총평
- 네 방향(→, ↘, ↓, ↙)만 보면 모든 오목 가능성을 커버하므로 방향 설정이 효율적입니다.
- `for ... else` 구문을 이용해 5개 연속 조건을 간결하게 처리한 점이 좋습니다.
- 그러나 `current_mok`는 방향 전환마다 초기화해야 하는데, 현재는 각 돌에서 첫 방향 탐색 후 값이 누적될 가능성이 있습니다.  
  (이 경우 실제 로직상 문제는 안 생기는 구조이지만, 의미상 혼동 가능)
- `n = N`처럼 함수 내부에서 전역 변수를 직접 참조하는 방식 대신 파라미터로 `n`을 받으면 재사용성이 좋아집니다.
<br><br>


# 보완점
## 1. `current_mok` 제거 및 반복 인덱스 기반 판정
- 어차피 방향 내에서 `k`를 1~4까지 이동했을 때 break 없이 끝나면 5목 이상이므로, 카운터 변수가 불필요합니다.
~~~python
for d in range(4):
    for k in range(1, 5):
        nr = r + dr[d] * k
        nc = c + dc[d] * k
        if not (0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 'o'):
            break
    else:
        return 'YES'
~~~

<br><br>


## 2. 전역 의존 제거
- `check_omok`이 `N` 전역을 사용하지 않도록 `n`을 인자로 받도록 변경.
~~~python
def check_omok(arr, n):
    ...
    for r in range(n):
        ...
        if not (0 <= nr < n and 0 <= nc < n ...):
            break
~~~

<br><br>


# 최종 코드 예시
~~~python
# 11315. 오목 판정

from typing import List

def check_omok(board: List[List[str]], n: int) -> str:
    """
    n x n 바둑판에서 'o'가 연속 5개 이상 있는지 확인.
    확인 방향: →, ↘, ↓, ↙
    """
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]

    for r in range(n):
        for c in range(n):
            if board[r][c] != 'o':
                continue
            for d in range(4):
                for k in range(1, 5):
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k
                    if not (0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'o'):
                        break
                else:
                    return 'YES'
    return 'NO'

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        board = [list(input().strip()) for _ in range(N)]
        print(f'#{tc} {check_omok(board, N)}')

if __name__ == "__main__":
    main()
~~~
