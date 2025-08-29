- [itertools 모듈](#itertools-모듈)
- [순열 (Permutations)](#순열-permutations)
  - [개념](#개념)
  - [`itertools.permutations`](#itertoolspermutations)
  - [Python 예시](#python-예시)
- [조합 (Combinations)](#조합-combinations)
  - [개념](#개념-1)
  - [`itertools.combinations`](#itertoolscombinations)
  - [Python 예시](#python-예시-1)
- [순열과 조합의 차이 요약](#순열과-조합의-차이-요약)

---

## itertools 모듈

- Python 표준 라이브러리로, 효율적인 반복(looping)을 위한 이터레이터(iterator)를 만드는 함수들을 제공한다.
- 순열, 조합, 중복 순열/조합 등 복잡한 반복 로직을 매우 간결하고 효율적으로 구현할 수 있게 도와준다.

---

## 순열 (Permutations)

### 개념
- 서로 다른 `n`개의 원소에서 `r`개를 **순서를 고려하여** 선택하거나 나열하는 경우의 수. (예: `(A, B)`와 `(B, A)`는 다른 경우로 취급)
- 순서가 중요하므로, "누가 뽑혔는가" 뿐만 아니라 "어떤 순서로 뽑혔는가"도 중요하다.

### `itertools.permutations`
- `permutations(iterable, r)` 형태로 사용한다.
- `iterable`에서 `r`개의 원소를 뽑아 만들 수 있는 모든 순열을 이터레이터 형태로 반환한다.

### Python 예시
```python
from itertools import permutations

items = ['A', 'B', 'C']

# items에서 2개를 뽑아 나열하는 모든 경우 (순열)
# P(3, 2) = 3 * 2 = 6
result = list(permutations(items, 2))

print(f"permutations(items, 2)의 결과: {result}")
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(f"경우의 수: {len(result)}") # 6
```

---

## 조합 (Combinations)

### 개념
- 서로 다른 `n`개의 원소에서 **순서를 고려하지 않고** `r`개를 선택하는 경우의 수. (예: `(A, B)`와 `(B, A)`는 같은 경우로 취급)
- 순서가 중요하지 않으므로, "누가 뽑혔는가"만이 중요하다.

### `itertools.combinations`
- `combinations(iterable, r)` 형태로 사용한다.
- `iterable`에서 `r`개의 원소를 뽑아 만들 수 있는 모든 조합을 이터레이터 형태로 반환한다.

### Python 예시
```python
from itertools import combinations

items = ['A', 'B', 'C']

# items에서 2개를 순서에 상관없이 뽑는 모든 경우 (조합)
# C(3, 2) = 3! / (2! * 1!) = 3
result = list(combinations(items, 2))

print(f"combinations(items, 2)의 결과: {result}")
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(f"경우의 수: {len(result)}") # 3
```

---

## 순열과 조합의 차이 요약

| 구분 | 순열 (Permutations) | 조합 (Combinations) |
| :--- | :--- | :--- |
| **핵심** | **순서**를 고려함 (나열) | **순서**를 고려하지 않음 (선택) |
| **결과 예시** | `(A, B)`와 `(B, A)`는 **다름** | `(A, B)`와 `(B, A)`는 **같음** |
| **사용 함수** | `itertools.permutations` | `itertools.combinations` |
| **주요 활용** | 순위 매기기, 역할 배정 등 | 대표 뽑기, 로또 번호 추첨 등 |
