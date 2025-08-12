- [총평](#총평)
- [보완점](#보완점)
  - [1. `calculate_flowers` 함수의 지역 변수 명명](#1-calculate_flowers-함수의-지역-변수-명명)
  - [2. `dr`, `dc` 방향 벡터를 튜플로 묶어서 zip 사용 가능](#2-dr-dc-방향-벡터를-튜플로-묶어서-zip-사용-가능)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문제의 요구사항을 정확히 구현한 코드로, 풍선 팡 터지기 범위를 delta 방식으로 잘 처리하고 있음
- 코드의 가독성과 함수 분리 수준도 우수하여, 유지보수나 재사용 측면에서도 안정적
- 반복문과 조건문도 잘 구성되어 있고, 코너케이스(범위를 벗어나는 경우)에 대한 처리도 적절함

<br><br>


# 보완점
## 1. `calculate_flowers` 함수의 지역 변수 명명
- `flowers`는 풍선 내부 꽃가루 수이자 터지는 범위를 의미하므로 다소 혼란을 줄 수 있음
- 의미 명확화를 위해 `power` 또는 `range_k`와 같은 이름으로 변경하면 좋음

```python
power = arr[r][c]
```

<br><br>

## 2. `dr`, `dc` 방향 벡터를 튜플로 묶어서 zip 사용 가능
- 더 파이썬답고 읽기 쉬운 방향 벡터 순회 형태를 만들 수 있음

```python
for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
    ...
```

다만 가독성 개선 차원일 뿐, 논리적 오류나 비효율이 있는 것은 아님

<br><br>


# 최종 코드 예시
```python
def calculate_flowers(arr, r, c):
    """
    해당 좌표에서 상하좌우로 터뜨렸을 때 총 꽃가루 수 반환
    """
    dr = [-1, 1, 0, 0]      # 상 하 좌 우
    dc = [0, 0, -1, 1]

    power = arr[r][c]
    popped = power

    for i in range(4):
        for k in range(1, power + 1):
            nr, nc = r + dr[i]*k, c + dc[i]*k
            if 0 <= nr < N and 0 <= nc < M:
                popped += arr[nr][nc]

    return popped

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flowers = 0
    for i in range(N):
        for j in range(M):
            popped = calculate_flowers(arr, i, j)
            if popped > max_flowers:
                max_flowers = popped

    print(f'#{tc} {max_flowers}')
```
