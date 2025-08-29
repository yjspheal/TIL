- [Greedy Algorithm (탐욕 알고리즘)](#greedy-algorithm-탐욕-알고리즘)
  - [개념](#개념)
  - [언제 사용할 수 있는가?](#언제-사용할-수-있는가)
  - [특징 및 한계](#특징-및-한계)
- [Baby-gin 문제](#baby-gin-문제)
  - [문제 정의](#문제-정의)
  - [해결 아이디어 (카운팅 배열 활용)](#해결-아이디어-카운팅-배열-활용)
  - [Python 예시](#python-예시)

---

## Greedy Algorithm (탐욕 알고리즘)

### 개념
- 각 단계에서 **그 순간에 가장 최적이라고 생각되는 선택(locally optimal choice)**을 하는 방식으로 최종 해답에 도달하는 알고리즘 설계 기법.
- 동적 계획법(Dynamic Programming)처럼 전체 문제의 최적해를 찾기 위해 모든 경우를 고려하지 않음.
- 일단 한 번 선택하면, 그 선택은 번복하지 않음.

### 언제 사용할 수 있는가?
탐욕 알고리즘은 다음 두 가지 속성이 만족되는 문제에 적용할 수 있다.

1.  **탐욕적 선택 속성 (Greedy Choice Property)**: 각 단계에서 한 국소적인 최적해가 최종적인 전역 최적해로 이어져야 한다.
2.  **최적 부분 구조 (Optimal Substructure)**: 문제의 최적해가 그 문제의 부분 문제들에 대한 최적해를 포함해야 한다.

### 특징 및 한계
- **장점**: 구현이 간단하고, 특정 문제에서는 매우 효율적으로 동작한다.
- **한계**: 항상 최적해를 보장하지는 않는다. 탐욕적으로 내린 결정이 전역적으로는 최적이 아닐 수 있기 때문이다. (예: 거스름돈 문제에서 특정 화폐 단위가 없는 경우)

---

## Baby-gin 문제

### 문제 정의
- 0부터 9까지의 숫자 카드 6장을 받아, 'run'과/와 'triplet'으로만 구성되어 있는지 판별하는 문제.
  - **run**: 세 숫자가 연속적인 경우 (예: 1, 2, 3)
  - **triplet**: 세 숫자가 모두 같은 경우 (예: 7, 7, 7)
- 6장의 카드가 1개의 run과 1개의 triplet, 또는 2개의 run, 또는 2개의 triplet으로 구성되면 "Baby-gin"이다.

### 해결 아이디어 (카운팅 배열 활용)
이 문제는 탐욕적 접근과 완전 검색 아이디어를 결합하여 효율적으로 풀 수 있다.

1.  **카운팅 배열 생성**: 숫자 카드의 개수를 세는 크기 10의 배열 `counts`를 만든다. (`counts[i]`는 숫자 `i`의 개수)
2.  **카드 개수 카운트**: 6장의 카드를 순회하며 `counts` 배열에 각 숫자의 개수를 기록한다.
3.  **Triplet 우선 확인 (탐욕적 접근)**: `counts` 배열을 순회하며, 특정 숫자가 3개 이상이면(`counts[i] >= 3`) triplet으로 간주하고 해당 카드를 3장 제거한다. triplet을 먼저 제거하는 것이 run을 형성할 카드를 남겨둘 가능성을 높여준다.
4.  **Run 확인**: 남은 카드들로 run을 확인한다. `counts[i]`, `counts[i+1]`, `counts[i+2]`가 모두 1개 이상이면 run으로 간주하고 카드를 1장씩 제거한다.
5.  **결과 판정**: 총 2개의 run 또는 triplet을 찾아냈다면 "Baby-gin"이다.

### Python 예시
```python
def is_baby_gin(cards):
    counts = [0] * 10
    for card in cards:
        counts[card] += 1

    gin_count = 0
    i = 0
    while i < 10:
        # 1. Triplet 확인
        if counts[i] >= 3:
            counts[i] -= 3
            gin_count += 1
            continue # 같은 숫자로 또 다른 triplet이 있을 수 있으므로

        # 2. Run 확인
        if i <= 7 and counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            gin_count += 1
            continue
        
        i += 1

    return gin_count == 2

# 예시
cards1 = [1, 2, 3, 1, 2, 3] # 2 runs -> True
cards2 = [4, 5, 6, 7, 7, 7] # 1 run, 1 triplet -> True
cards3 = [1, 1, 1, 2, 2, 2] # 2 triplets -> True
cards4 = [1, 2, 3, 4, 5, 6] # 2 runs -> True
cards5 = [1, 1, 2, 2, 3, 3] # False

print(f"[1, 2, 3, 1, 2, 3] is Baby-gin? {is_baby_gin(cards1)}")
print(f"[4, 5, 6, 7, 7, 7] is Baby-gin? {is_baby_gin(cards2)}")
print(f"[1, 1, 2, 2, 3, 3] is Baby-gin? {is_baby_gin(cards5)}")
```
