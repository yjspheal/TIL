# 기존 코드
~~~python
# 1211. [S/W 문제해결 기본] 2일차 - Ladder2

# import sys
#
# sys.stdin = open('input.txt')


def down_ladder(arr, c):
    """
    arr[0][c] 지점에서 사다리를 내려가는 루트에 드는 길이를 구하여 return
    Args:
        arr (list): 1, 0으로 이루어진 100x100 행렬
        c (int): 시작점의 x값
    Returns:
        int: 루트 길이
    """
    r = 0  # 시작점의 행
    route_length = 0  # 루트의 길이 계산

    while r < 100:  # 바닥에 닿기 전까지
        if arr[r][c - 1] == 1:  # 왼쪽에 길이 있다면
            while arr[r][c - 1] == 1:  # 왼쪽 끝까지 간다
                c -= 1
                route_length += 1  # 루트 길이에 1 추가

        elif arr[r][c + 1] == 1:  # 오른쪽에 길이 있다면
            while arr[r][c + 1] == 1:  # 오른쪽 끝까지 간다
                c += 1
                route_length += 1  # 루트 길이에 1 추가

        r += 1  # 아래로 한칸 간다
        route_length += 1  # 루트 길이에 1 추가

        while r < 100 and arr[r][c - 1] == 0 and arr[r][c + 1] == 0:  # 바닥이 아니고 양쪽이 벽이라면
            r += 1
            route_length += 1  # 사다리가 나오거나 받가이 나올 때까지 밑으로 간다

    return route_length


T = 10
for _ in range(1, T + 1):
    tc = input()
    ladder = []  # 사다리 정보를 담은 이차원 배열

    for __ in range(100):  # 사다리는 100x100
        # 양쪽에 벽을 하나씩 둔다(셀렉션)
        ladder.append([0] + list(map(int, input().split())) + [0])

    start_points = []  # 시작점 인덱스들을 모을 리스트
    for i in range(101):
        if ladder[0][i] == 1:  # 시작점이라면 인덱스 추가
            start_points.append(i)

    # 초기값 설정
    shortest_length = down_ladder(ladder, start_points[0])
    shortest_x = start_points[0]

    for start_point in start_points[1:]:  # 첫번째 건 위에서 했으므로
        current_length = down_ladder(ladder, start_point)  # 이번 start point의 루트 길이

        if current_length < shortest_length:  # 더 짧다면 루트 길이와 x를 업데이트
            shortest_length = current_length
            shortest_x = start_point

    print(f'#{tc} {shortest_x - 1}')  # 앞에 셀렉션 제외
~~~
<br><br>


# 총평
- 좌/우가 보이면 끝까지 가로로 이동한 뒤 한 칸 아래로 내려가는 전형적인 사다리 탐색을 잘 구현했습니다(좌 우 우선순위가 명확).
- 좌우 경계는 양쪽에 0을 패딩(sentinel)해 안전하게 접근합니다.
- 다만 `while r < 100` 고정, `start_points` 탐색 범위, 그리고 “수직으로 연속해서 내려가는 보조 while” 등 **하드코딩/중복 로직**이 있어 단순화할 여지가 큽니다.
- 행 길이/열 길이를 **동적으로** 취하면 재사용성이 좋아지고, 가독성도 향상됩니다.
<br><br>


# 보완점
## 1. 수직 이동 보조 while 제거로 로직 단순화
- 현재는 아래로 한 칸 이동한 뒤, 양옆이 0인 동안 추가로 계속 내려가는 `while`이 있습니다.
- 하지만 메인 루프가 다시 반복되며 동일하게 “좌/우가 있으면 가로로, 아니면 내려가기”를 수행하므로 **보조 while 없이도** 동일한 결과를 얻습니다.
- 불필요한 중첩을 줄이면 버그 포인트와 인덱싱 실수를 줄일 수 있습니다.

~~~python
def down_ladder(arr, c):
    R, C = len(arr), len(arr[0])
    r = 0
    dist = 0
    while r < R - 1:  # 마지막 행에 도달하기 전까지
        # 왼쪽으로 가능한 만큼
        while arr[r][c - 1] == 1:
            c -= 1
            dist += 1
        # 오른쪽으로 가능한 만큼
        while arr[r][c + 1] == 1:
            c += 1
            dist += 1
        # 아래로 한 칸
        r += 1
        dist += 1
    return dist
~~~


<br><br>


## 2. 하드코딩(100) 제거 및 시작점 스캔 범위 명확화
- 입력이 100x100이라도 함수는 `len(arr)`를 사용해 더 일반적으로 만듭니다.
- 시작점은 좌/우 패딩을 제외한 **1..C-2** 범위에서만 확인하면 됩니다. (패딩은 반드시 0)

~~~python
# 시작점 수집 (첫 행)
start_points = [c for c in range(1, C - 1) if ladder[0][c] == 1]
~~~


<br><br>


## 3. 구조화 & 가독성(타입 힌트, main 분리)
- 테스트케이스 루프와 한 케이스 처리 로직을 분리해 재사용/디버깅에 유리하게 합니다.
- 타입 힌트를 추가해 의도를 명확히 합니다.

<br><br>


# 최종 코드 예시
~~~python
# 1211. [S/W 문제해결 기본] 2일차 - Ladder2

# 제출 시 필요하다면 아래 사용
# import sys
# sys.stdin = open('input.txt', 'r')

from typing import List

def down_ladder(grid: List[List[int]], c: int) -> int:
    """
    좌/우가 연결되어 있으면 해당 방향으로 끝까지 이동 후,
    아래로 한 칸 내려가는 동작을 반복하여 바닥(마지막 행)에 도달할 때까지의 이동 거리 반환.
    grid는 좌/우에 0으로 패딩되어 있어야 한다.
    """
    R, C = len(grid), len(grid[0])
    r = 0
    dist = 0
    # 마지막 행에 도달하기 전까지
    while r < R - 1:
        # 왼쪽으로 가능한 만큼 이동
        while grid[r][c - 1] == 1:
            c -= 1
            dist += 1
        # 오른쪽으로 가능한 만큼 이동
        while grid[r][c + 1] == 1:
            c += 1
            dist += 1
        # 아래로 한 칸 이동
        r += 1
        dist += 1
    return dist

def solve_one_case() -> int:
    """
    한 테스트케이스를 읽어, 가장 짧은 경로 길이를 내는 시작점의 x(0-based, 패딩 제외)를 반환.
    길이가 동일하면 '더 큰 x'가 아닌 '더 작은 x'가 정답인지 문제 정책에 따라 tie-break가 있으나
    SWEA 1211에서는 동일 길이 시 더 왼쪽(작은 x)을 선택하도록 입력이 구성됩니다.
    """
    # 테스트케이스 번호(숫자)를 한 줄 읽음 (문자열이어도 무방)
    _tc = input().strip()

    # 사다리 그리드 읽기 및 좌/우 패딩 추가
    grid: List[List[int]] = []
    for _ in range(100):
        row = list(map(int, input().split()))
        grid.append([0] + row + [0])

    R, C = len(grid), len(grid[0])

    # 첫 행에서 시작점(1이 있는 열) 수집 — 패딩 제외
    start_points = [c for c in range(1, C - 1) if grid[0][c] == 1]

    # 초기값 설정
    best_c = start_points[0]
    best_len = down_ladder(grid, best_c)

    # 나머지 시작점들 비교
    for c in start_points[1:]:
        cur_len = down_ladder(grid, c)
        if cur_len < best_len:
            best_len = cur_len
            best_c = c
        # 길이가 같을 때의 tie-break(더 왼쪽 우선)가 필요하다면 아래 조건 사용:
        # elif cur_len == best_len and c < best_c:
        #     best_c = c

    # 문제 출력 형식에 맞게, 좌/우 패딩을 제외한 0-based 인덱스로 출력
    return best_c - 1

def main() -> None:
    T = 10
    for _ in range(T):
        ans = solve_one_case()
        print(f'#{_ + 1} {ans}')

if __name__ == "__main__":
    main()
~~~
