- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 numpy 의존성 제거 및 순수 Python 사용](#1-불필요한-numpy-의존성-제거-및-순수-python-사용)
  - [2. max\_multsum 초기화 로직 강화](#2-max_multsum-초기화-로직-강화)
- [최종 코드 예시](#최종-코드-예시)

<br>

# 총평
- 알고리즘(슬라이딩 윈도우 기반 최대 내적 합 계산) 구현이 명확하고 가독성이 좋음
- numpy를 활용해 벡터 연산을 시도했으나, 매 반복마다 배열 생성이 이루어져 불필요한 오버헤드가 발생
- 모든 가능한 내적 합이 음수일 때도 0으로 처리되어 잘못된 결과를 반환할 위험이 있음

<br>

# 보완점
## 1. 불필요한 numpy 의존성 제거 및 순수 Python 사용
- `np.array` 변환을 반복하는 대신 `sum`과 `zip`을 사용해 내적을 계산하도록 변경
```python
curr = sum(a * b for a, b in zip(A, B[shift:shift+N]))
```

<br>

## 2. max_multsum 초기화 로직 강화
- 가능한 모든 계산 결과가 음수인 경우에도 올바르게 동작하도록 `max_multsum`을 `-float('inf')`로 초기화하거나 첫 계산 값으로 설정

<br>

# 최종 코드 예시
```python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
        N, M = M, N

    max_multsum = -float('inf')
    for shift in range(M - N + 1):
        curr = sum(a * b for a, b in zip(A, B[shift:shift+N]))
        max_multsum = max(max_multsum, curr)

    print(f"#{tc} {max_multsum}")
```
