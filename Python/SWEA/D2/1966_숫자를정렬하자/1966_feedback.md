- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 버블정렬과 선택정렬의 range 범위 개선 및 가독성 향상](#1-버블정렬과-선택정렬의-range-범위-개선-및-가독성-향상)
  - [2. 내장 정렬 사용 예시 추가](#2-내장-정렬-사용-예시-추가)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 1966_숫자를정렬하자.

def bubble_sort(arr, n):
    """
    버블정렬하는 함수
    Args:
        arr(list): 숫자 리스트
        n (int): 리스트 길이
    Returns:
        list: 정렬된 리스트
    """
    # 앞자리부터 순회하며
    for i in range(n, 1, -1):  # 매 순회마다 가장 오른쪽값이 채워지므로 상한값이 1씩 줆
        for j in range(1, i):
            if arr[j] < arr[j - 1]:  # 이전것보다 값이 작다면
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # swap

    return arr


def select_sort(arr, n):
    """
    선택정렬하는 함수
    Args:
        arr(list): 숫자 리스트
        n (int): 리스트 길이
    Returns:
        list: 정렬된 리스트
    """
    for i in range(n, 1, -1):  # 매 순회마다 가장 오른쪽값이 채워지므로 상한값이 1씩 줆
        max_idx = 0  # 최대 인덱스 지정
        for j in range(i):
            if arr[j] > arr[max_idx]:  # j번쨰 원소 값이 더 크다면
                max_idx = j  # max idx 업데이트

        arr[i - 1], arr[max_idx] = arr[max_idx], arr[i - 1]

    return arr


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())  # 들어올 숫자의 갯수
    nums = list(map(int, input().split()))  # 숫자 리스트 받기

    # sorted_nums = bubble_sort(nums, N)
    sorted_nums = select_sort(nums, N)

    print(f'#{tc}', *sorted_nums)
~~~
<br><br>


# 총평
- 버블정렬과 선택정렬 두 가지 구현이 모두 정확하며, 주석이 풍부해 이해하기 쉽습니다.
- `bubble_sort`의 루프 인덱스 범위와 `select_sort`의 최대값 위치 갱신 로직 모두 올바르게 구현되었습니다.
- 다만 Python 내장 정렬을 쓰면 훨씬 빠르고 간결하며, O(N log N) 시간복잡도를 가집니다.
- `range`의 매개변수 의미(시작값, 끝값, 스텝)와 알고리즘 시간복잡도 설명이 코드에 더해지면 학습용으로 완성도가 높아집니다.

<br><br>


# 보완점
## 1. 버블정렬과 선택정렬의 range 범위 개선 및 가독성 향상
현재 `range(n, 1, -1)` 사용은 동작에 문제는 없지만, 학습 목적이라면 `range(n-1, 0, -1)` 또는 `range(n)` 구조가 직관적일 수 있습니다.
~~~python
for i in range(n-1, 0, -1):  # i는 이번 패스에서 비교할 마지막 인덱스
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
~~~

<br><br>


## 2. 내장 정렬 사용 예시 추가
실제 실무나 대회에서는 직접 구현보다 `sorted()` 또는 `.sort()`를 활용하는 것이 효율적입니다.
~~~python
sorted_nums = sorted(nums)
~~~
이렇게 하면 O(N log N) 시간복잡도로 빠르고 안정적으로 정렬됩니다.

<br><br>


# 최종 코드 예시
~~~python
# 1966_숫자를정렬하자

def bubble_sort(arr):
    """버블정렬: O(n^2)"""
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def select_sort(arr):
    """선택정렬: O(n^2)"""
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_idx = 0
        for j in range(i+1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        nums = list(map(int, input().split()))
        
        # 학습용 정렬
        # sorted_nums = bubble_sort(nums[:])
        sorted_nums = select_sort(nums[:])
        
        # 실무용 정렬
        # sorted_nums = sorted(nums)
        
        print(f"#{tc}", *sorted_nums)

if __name__ == "__main__":
    main()
~~~
