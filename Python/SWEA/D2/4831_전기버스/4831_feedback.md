- [총평](#총평)
- [보완점](#보완점)
  - [1. 전역 변수(`k`) 의존성 제거 및 함수 파라미터화](#1-전역-변수k-의존성-제거-및-함수-파라미터화)
  - [2. 불필요한 리스트 삭제(`del`) 제거 및 인덱스 기반 그리디로 간소화](#2-불필요한-리스트-삭제del-제거-및-인덱스-기반-그리디로-간소화)
- [최종 코드 예시](#최종-코드-예시)


<br>

# 총평
- 충전소 간 거리를 계산한 뒤, 일정 간격(`k`)으로 누적하여 최소 충전 횟수를 구하는 그리디 알고리즘을 구현함
- 구간 거리가 `k`를 초과할 경우 즉시 `0`을 반환하여 불가능 케이스를 처리함
- 전체 흐름이 논리적으로 구성되어 문제 요구사항을 만족함

<br><br>

# 보완점
## 1. 전역 변수(`k`) 의존성 제거 및 함수 파라미터화
- `count_charging_station` 함수 내부에서 전역 `k`에 의존하고 있어 함수 재사용성이 떨어집니다. `k`를 인자로 받아 처리하도록 수정하세요.

```python
def count_charging_station(stations, k):
    ...
```  

<br><br>
## 2. 불필요한 리스트 삭제(`del`) 제거 및 인덱스 기반 그리디로 간소화
- `distances` 리스트에 대해 `del distances[:j]` 연산은 O(n) 비용을 초래하므로, 포인터를 이용한 선형 그리디 탐색으로 대체하세요.
<br><br>
- 현재 위치에서 최대 거리 내에 있는 마지막 충전소로 이동하는 방식으로 구현하면 O(M) 시간에 처리할 수 있습니다.

```python
def count_charging_station(stations, k):
    current = 0  # 현재 인덱스
    count = 0    # 충전 횟수
    for i in range(1, len(stations)):
        # 이동 거리가 k 초과 시, 앞선 충전소에서 충전
        if stations[i] - stations[current] > k:
            current = i - 1
            count += 1
            # 충전소 사이 간격이 k를 초과하면 불가능
            if stations[i] - stations[current] > k:
                return 0
    return count
```  

<br><br>
# 최종 코드 예시
```python
import sys

input = sys.stdin.readline

def count_charging_station(stations, k):
    current = 0
    count = 0
    for i in range(1, len(stations)):
        # k를 넘으면 직전에서 충전
        if stations[i] - stations[current] > k:
            current = i - 1
            count += 1
            # 한 구간이 k보다 크면 불가
            if stations[i] - stations[current] > k:
                return 0
    return count


def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        k, N, M = map(int, input().split())
        stations = [0] + list(map(int, input().split())) + [N]
        result = count_charging_station(stations, k)
        print(f"#{tc} {result}")

if __name__ == '__main__':
    solve()
```