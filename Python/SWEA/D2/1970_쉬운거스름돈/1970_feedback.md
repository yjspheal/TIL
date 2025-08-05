- [총평](#총평)
- [보완점](#보완점)
  - [1. 리스트 언패킹 및 `print` 간결화](#1-리스트-언패킹-및-print-간결화)
  - [2. 타입 힌트 및 상수화](#2-타입-힌트-및-상수화)
- [최종 코드 예시](#최종-코드-예시)



# 총평
- `calculate_bills` 함수가 큰 단위에서 작은 단위까지 차례로 나누어 몫과 나머지를 계산하며 올바른 지폐 조합을 도출함
- `//` 및 `%` 연산을 활용해 직관적이고 효율적인 구현을 보여줌
- 모듈화된 함수와 메인 루프 분리로 가독성과 재사용성을 확보함

<br><br>

# 보완점

## 1. 리스트 언패킹 및 `print` 간결화
- 별도의 루프 없이 `print(*counts)`를 사용해 지폐 개수를 한 줄에 출력할 수 있습니다.
- `f'#{tc}'`와 `*counts`를 한 번에 출력할 수도 있습니다.

```python
print(f"#{tc}", *counts)
```

<br><br>
## 2. 타입 힌트 및 상수화
- `calculate_bills` 함수에 입력과 반환 타입 힌트를 추가해 IDE 및 정적 분석 도구 활용을 강화합니다.
- 지폐 단위를 모듈 상단의 상수로 정의하면 유지보수가 용이해집니다.

```python
from typing import List

BILLS: List[int] = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def calculate_bills(price: int) -> List[int]:
    bill_counts: List[int] = []
    for bill in BILLS:
        count = price // bill
        bill_counts.append(count)
        price %= bill
    return bill_counts
```

<br><br>
# 최종 코드 예시
```python
import sys
from typing import List

input = sys.stdin.readline
BILLS: List[int] = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def calculate_bills(price: int) -> List[int]:
    bill_counts: List[int] = []
    for bill in BILLS:
        bill_counts.append(price // bill)
        price %= bill
    return bill_counts


def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        charge = int(input().strip())
        counts = calculate_bills(charge)
        print(f"#{tc}", *counts)

if __name__ == '__main__':
    solve()
```