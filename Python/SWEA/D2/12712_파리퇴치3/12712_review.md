- [총평](#총평)
- [보완점](#보완점)
  - [1. 이중 for 루프로 명시적 순회](#1-이중-for-루프로-명시적-순회)
  - [2. 방향 벡터로 중복 코드 제거](#2-방향-벡터로-중복-코드-제거)
- [최종 코드 예시](#최종-코드-예시)

<br>

# 총평
- 중심 인덱스를 1차원 `center` 루프에서 `c_row = center // N`, `c_col = center % N`로 변환하여 2차원 순회를 구현한 로직이 적절함
- +/× 패턴을 모두 고려하여 정확하게 파리 개수를 집계함
- 기존 `% 5` → `% N` 수정으로 모듈 연산 버그가 올바르게 해결됨

<br>

# 보완점
## 1. 이중 for 루프로 명시적 순회
- 1차원 `center` 루프 대신 `for r in range(N): for c in range(N):` 구조를 사용해 가독성을 향상
```python
for r in range(N):
    for c in range(N):
        # 중심 좌표(r, c)에서 처리
```

<br>

## 2. 방향 벡터로 중복 코드 제거
- 상하좌우, 대각선 방향을 미리 정의한 리스트(`plus_dirs`, `cross_dirs`)로 공통 로직 일반화
```python
plus_dirs  = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cross_dirs = [(-1,-1),(-1, 1),(1, -1),(1, 1)]
for dr, dc in plus_dirs:
    for dist in range(1, M):
        nr, nc = r + dr * dist, c + dc * dist
        if 0 <= nr < N and 0 <= nc < N:
            plus_sum += fly[nr][nc]
```

<br>

# 최종 코드 예시
```python
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    plus_dirs  = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cross_dirs = [(-1,-1),(-1, 1),(1, -1),(1, 1)]

    for r in range(N):
        for c in range(N):
            plus_sum  = fly[r][c]
            cross_sum = fly[r][c]
            for dr, dc in plus_dirs:
                for dist in range(1, M):
                    nr, nc = r + dr * dist, c + dc * dist
                    if 0 <= nr < N and 0 <= nc < N:
                        plus_sum += fly[nr][nc]
            for dr, dc in cross_dirs:
                for dist in range(1, M):
                    nr, nc = r + dr * dist, c + dc * dist
                    if 0 <= nr < N and 0 <= nc < N:
                        cross_sum += fly[nr][nc]
            max_fly = max(max_fly, plus_sum, cross_sum)

    print(f"#{tc} {max_fly}")
```
