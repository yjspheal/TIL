- [총평](#총평)
- [보완점](#보완점)
  - [1. 내부 반복문 최적화 필요](#1-내부-반복문-최적화-필요)
  - [2. 의미 없는 `else: continue` 구문 제거 가능](#2-의미-없는-else-continue-구문-제거-가능)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문제 요구사항에 맞게 2, 3, 5, 7, 11로만 소인수분해하여 각 소인수의 지수를 구하는 구조는 적절함
- 전체 흐름 및 로직은 간단 명료하며, 초보자도 이해하기 좋은 구조로 짜여 있음
- 다만, **불필요한 반복**과 **비효율적인 로직 흐름**이 있어 개선 가능성이 있음

<br><br>

# 보완점
## 1. 내부 반복문 최적화 필요
현재 `while N > 1` 루프 안에서 `for`문이 매번 순회되는데, 나눠지지 않는 경우에도 무조건 순회되므로 **불필요한 소수들까지 계속 검사**하게 됨.

이런 경우 `while`문을 각 소수마다 따로 구성하면 훨씬 깔끔하고 효율적으로 작성 가능.

```python
for i, prime in enumerate([2, 3, 5, 7, 11]):
    while N % prime == 0:
        N //= prime
        prime_counts[i] += 1
```

- 이처럼 바꾸면 각 소수에 대해 나눠지는 동안만 반복되므로 효율적임

<br><br>

## 2. 의미 없는 `else: continue` 구문 제거 가능
`else: continue`는 아무 의미 없이 다음 루프로 넘어가는 동작만 하므로 제거해도 동작에 전혀 영향 없음.

- 불필요한 라인 수를 줄이고 가독성을 높이기 위해 삭제하는 것이 좋음

<br><br>

# 최종 코드 예시
```python
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prime_counts = [0] * 5
    primes = [2, 3, 5, 7, 11]

    for i, prime in enumerate(primes):
        while N % prime == 0:
            N //= prime
            prime_counts[i] += 1

    print(f'#{tc}', *prime_counts)
```
