- [총평](#총평)
- [보완점](#보완점)
  - [1. 이웃 건물 최대값 계산 간소화](#1-이웃-건물-최대값-계산-간소화)
  - [2. 값 계산 표현식 단순화](#2-값-계산-표현식-단순화)
  - [3. 변수명 최적화](#3-변수명-최적화)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문제 요구사항(각 빌딩이 양쪽 두 채 건물보다 얼마나 더 높은지 합산)을 올바르게 구현함
- 이중 `for` 루프를 사용해 각 빌딩의 좌우 두 채를 순회하며 최대값을 계산하는 논리가 명확함
- `nice_view_count` 집계 방식이 간결하고 직관적임

<br><br>

# 보완점
## 1. 이웃 건물 최대값 계산 간소화
현재 `for j in range(idx-2, idx+3)`와 `if j == idx: continue` 로 구현한 부분을, 파이썬의 슬라이스와 `max` 함수를 활용해 한 줄로 줄일 수 있습니다.
```python
left_max = max(buildings[idx-2:idx])
right_max = max(buildings[idx+1:idx+3])
neighbor_max = max(left_max, right_max)
```
이렇게 하면 인덴트와 조건문이 줄어들어 가독성이 향상됩니다.

<br><br>
## 2. 값 계산 표현식 단순화
`if current_building - max_building >= 0 else 0` 조건문 대신 `max(0, current_building - neighbor_max)`를 사용하면 더 직관적입니다.
```python
nice_view_count += max(0, current_building - neighbor_max)
```

<br><br>
## 3. 변수명 최적화
- `building_count`보다 `n` 또는 `num_buildings` 같이 간결한 이름을 사용하면 코드가 덜 장황해집니다.

<br><br>
# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

T = 10
for tc in range(1, T + 1):
    n = int(input().strip())
    heights = list(map(int, input().split()))
    view_count = 0

    for i in range(2, n - 2):
        h = heights[i]
        left_max = max(heights[i-2:i])
        right_max = max(heights[i+1:i+3])
        neighbor_max = max(left_max, right_max)
        view_count += max(0, h - neighbor_max)

    print(f"#{tc} {view_count}")
```  