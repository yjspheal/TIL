- [1. 퀵 정렬(Quick Sort)이란?](#1-퀵-정렬quick-sort이란)
- [2. 분할(Partition) 과정](#2-분할partition-과정)
- [3. 파이썬 구현](#3-파이썬-구현)
- [4. 시간 복잡도](#4-시간-복잡도)

---

## 1. 퀵 정렬(Quick Sort)이란?

- `분할 정복(Divide and Conquer)` 알고리즘의 대표적인 예시
- 배열 내에서 하나의 기준점(`피벗, pivot`)을 설정
- 피벗을 기준으로 작은 값들은 왼쪽, 큰 값들은 오른쪽으로 분할
- 분할된 두 개의 부분 배열에 대해 재귀적으로 동일한 과정을 반복하여 정렬함

## 2. 분할(Partition) 과정

- 가장 대표적인 `로무토 분할(Lomuto partition)` 방식
    - 배열의 가장 오른쪽 원소를 피벗으로 선택
    - 포인터를 사용하여 피벗보다 작은 원소들을 배열의 왼쪽으로 이동시킴
    - 모든 원소 순회가 끝나면, 포인터의 다음 위치에 피벗을 배치함

## 3. 파이썬 구현

```python
def partition(arr, low, high):
    # 피벗을 배열의 가장 오른쪽 원소로 선택
    pivot = arr[high]
    
    # 피벗보다 작은 원소들을 저장할 위치를 가리키는 인덱스
    i = low - 1
    
    for j in range(low, high):
        # 현재 원소가 피벗보다 작으면
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # 스왑
            
    # 분할이 끝난 후, 피벗을 올바른 위치로 이동
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # 분할 인덱스 계산
        pi = partition(arr, low, high)
        
        # 분할된 두 부분 배열에 대해 재귀적으로 퀵 정렬 호출
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# 예시
my_list = [10, 7, 8, 9, 1, 5]
quick_sort(my_list, 0, len(my_list) - 1)
# 정렬된 리스트: [1, 5, 7, 8, 9, 10]
```

## 4. 시간 복잡도

- **평균**: `O(n log n)`
    - 피벗이 분할을 균형있게 할 때의 시간 복잡도
- **최악**: `O(n^2)`
    - 피벗이 항상 가장 작거나 가장 큰 원소로 선택될 경우 발생
    - (예: 이미 정렬된 배열에서 항상 마지막 원소를 피벗으로 선택하는 경우)
    - 이러한 불균형한 분할로 인해 재귀 호출의 깊이가 n에 가까워짐
