# 기존 코드
~~~python
# 20230. 풍선팡 보너스게임2

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    row_sums = [0] * N  # 행, 열별 합 담는 리스트
    col_sums = [0] * N

    # 풍선 숫자 정보를 담은 이차원배열
    balloons = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            # 합 생성
            row_sums[r] += balloons[r][c]
            col_sums[c] += balloons[r][c]

    max_score = 0
    for r in range(N):
        for c in range(N):
            score = row_sums[r] + col_sums[c] - balloons[r][c]

            if score > max_score:
                max_score = score
    print(f'#{tc} {max_score}')
~~~
<br><br>


# 총평
- 정답 로직(각 칸 점수 = 해당 행 합 + 해당 열 합 - 칸 값)을 정확히 구현했습니다.
- 시간복잡도는 O(N^2)로 최적 수준이며, 불필요한 3중 루프가 없어 효율적입니다.
- 행/열 합 계산을 **입력과 동시에** 처리하면 별도의 합산 루프 1회를 줄여 조금 더 깔끔해집니다.
- 한 번 더 가독성을 높이기 위해 list comprehension / `max` 표현식, 타입 힌트, 함수화 등을 적용할 수 있습니다.
<br><br>


# 보완점


## 1. 입력과 동시에 합 계산해 루프 단순화
- 현재는 그리드를 모두 입력받은 뒤 합을 계산합니다. 입력하면서 `row_sums`와 `col_sums`를 갱신하면 합산용 이중 루프가 사라져 코드가 간결해집니다.
- 최종 최대값은 2중 루프 또는 `max()` 내 포괄적 리스트/제너레이터로 구할 수 있습니다.

~~~python
N = int(input())
balloons = []
row_sums = [0] * N
col_sums = [0] * N

for r in range(N):
    row = list(map(int, input().split()))
    balloons.append(row)
    s = sum(row)
    row_sums[r] = s
    for c, v in enumerate(row):
        col_sums[c] += v

max_score = -float('inf')
for r in range(N):
    for c in range(N):
        score = row_sums[r] + col_sums[c] - balloons[r][c]
        if score > max_score:
            max_score = score
~~~

- 또는 더 간단히:
~~~python
max_score = max(row_sums[r] + col_sums[c] - balloons[r][c]
                for r in range(N) for c in range(N))
~~~

<br><br>


# 최종 코드 예시
~~~python
# 20230. 풍선팡 보너스게임2

from typing import List

def solve_case() -> int:
    N = int(input())

    balloons: List[List[int]] = []
    row_sums: List[int] = [0] * N
    col_sums: List[int] = [0] * N

    # 입력과 동시에 행/열 합 갱신
    for r in range(N):
        row = list(map(int, input().split()))
        balloons.append(row)
        row_sums[r] = sum(row)
        for c, v in enumerate(row):
            col_sums[c] += v

    # 최대 점수 계산 (안전한 초기화)
    max_score = -float('inf')
    for r in range(N):
        rr = row_sums[r]
        row = balloons[r]
        for c in range(N):
            score = rr + col_sums[c] - row[c]
            if score > max_score:
                max_score = score

    return max_score

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        ans = solve_case()
        print(f'#{tc} {ans}')

if __name__ == "__main__":
    main()
~~~
