# 총평
- 문제에서 요구하는 행, 열, 대각선 합의 최대값을 잘 계산한 코드임
- `row_sum`, `col_sum`, `right_diagonal_sum`, `left_diagonal_sum`을 반복문 안에서 동시에 관리하는 방식은 효율적이며 불필요한 반복도 없음
- 전반적으로 성능과 구조 모두 적절하게 구현되어 있음

<br><br>


# 보완점
## 1. 대각선 합 계산 방식 보완
- `right_diagonal_sum`, `left_diagonal_sum` 계산을 `i == j` 또는 `i == N - 1 - j` 조건으로 확인하는 방식은 틀리지 않았으나, 중복 누적되는 구조임
- `for j in range(N)` 루프 안에서 두 조건을 매번 검사하는 대신, `for i in range(N)` 루프 자체에서 따로 한 번만 계산하는 방식이 효율적임

```python
for i in range(N):
    row_sum = 0
    col_sum = 0
    for j in range(N):
        row_sum += arr[i][j]
        col_sum += arr[j][i]
    max_sum = max(max_sum, row_sum, col_sum)

    # i번째만 이용해 대각선도 별도로 처리
    right_diagonal_sum += arr[i][i]
    left_diagonal_sum += arr[i][N - 1 - i]
```

<br><br>


## 2. `max_sum` 갱신 위치 재조정
- 현재 구조는 `for num in [...]` 으로 묶어서 4개의 합을 모두 비교하지만, 대각선 합은 여러 번 중복 비교될 수 있음
- 마지막에 따로 `max_sum`과 `right_diagonal_sum`, `left_diagonal_sum`을 비교해주는 방식이 더 명확함

```python
max_sum = max(max_sum, right_diagonal_sum, left_diagonal_sum)
```

<br><br>


# 최종 코드 예시
```python
T = 10
N = 100

for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    right_diagonal_sum = 0
    left_diagonal_sum = 0

    for i in range(N):
        row_sum = 0
        col_sum = 0
        for j in range(N):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        max_sum = max(max_sum, row_sum, col_sum)

        right_diagonal_sum += arr[i][i]
        left_diagonal_sum += arr[i][N - 1 - i]

    max_sum = max(max_sum, right_diagonal_sum, left_diagonal_sum)
    print(f'#{tc} {max_sum}')
```
