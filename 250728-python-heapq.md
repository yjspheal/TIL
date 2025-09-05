- [1. heapq 모듈이란?](#1-heapq-모듈이란)
- [2. 최소 힙(Min Heap)](#2-최소-힙min-heap)
- [3. 주요 함수](#3-주요-함수)
- [4. 최대 힙(Max Heap) 구현](#4-최대-힙max-heap-구현)

---

## 1. heapq 모듈이란?

- 파이썬에서 `힙(Heap)` 자료구조를 구현하기 위해 제공하는 표준 라이브러리
- 일반적인 리스트를 최소 힙처럼 다룰 수 있게 도와줌

## 2. 최소 힙(Min Heap)

- `heapq`는 기본적으로 `최소 힙`으로 구현됨
  - 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같은 완전 이진 트리
- `heap[0]`은 항상 가장 작은 값을 가짐

## 3. 주요 함수

- `heapq.heappush(heap, item)`
    - 힙에 원소를 추가
- `heapq.heappop(heap)`
    - 힙에서 가장 작은 원소를 제거하고 반환
- `heapq.heapify(list)`
    - 일반 리스트를 제자리에서(in-place) 힙으로 변환

```python
import heapq

# 힙에 원소 추가
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
# heap: [1, 4, 7]

# 힙에서 원소 제거
smallest = heapq.heappop(heap) # 1 반환
# heap: [4, 7]

# 리스트를 힙으로 변환
my_list = [3, 5, 2, 8, 4]
heapq.heapify(my_list)
# my_list: [2, 4, 3, 8, 5]
```

## 4. 최대 힙(Max Heap) 구현

- `heapq`는 최대 힙을 직접 지원하지 않음
- 따라서, 값에 `음수 부호(-)`를 붙여서 힙에 추가하는 방식으로 구현
- 값을 꺼낼 때 다시 부호를 변경하여 원래 값으로 복원

```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
max_heap = []

for num in nums:
    heapq.heappush(max_heap, -num)

# max_heap: [-8, -5, -7, -3, -1, -4]

# 최댓값 꺼내기
largest = -heapq.heappop(max_heap) # 8 반환
```
