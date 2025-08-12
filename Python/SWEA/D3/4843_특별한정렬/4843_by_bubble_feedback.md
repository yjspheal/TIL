- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 두 번째 버블정렬 제거](#1-불필요한-두-번째-버블정렬-제거)
  - [2. 내장 정렬 사용으로 간결화](#2-내장-정렬-사용으로-간결화)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
import sys

sys.stdin = open("sample_input.txt", "r")


# # sys.stdin = open("input.txt", "r")

def specific_sort(arr, len_arr):
    """
    정수로 이루어진 리스트를 인자로 받아, 오름차순으로 정렬하여 return
    단, 앞 5개와 뒤 5개만 진행한다.

    Args:
        arr (list): 정수로 이루어진 리스트. 정렬 전 원본
        len_arr (int): arr 길이

    Returns:
        list: 정렬된 arr의 앞 10개만 담은 list
    """

    # 버블정렬(오름차순)을 5번 진행할 것
    for i in range(5):
        for j in range(1, len_arr - i):  # i 전까지 가야, 이전에 정렬한걸 건드리지 않음
            if arr[j] < arr[j - 1]:  # 이전거보다 지금이 작으면
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # 바꿔준다

    # 버블정렬(내림차순)을 5번 진행할 것
    # 왜 내림차순을 반대로해요? 오름차순만 하면 되지 않나요?
    # 정수 배열 길이가 매우 길 경우를 대비하여...효율을위해

    for i in range(5):
        for j in range(len_arr - 1, i, -1):  # len_arr - 6를 해줘도 되지만 5개정도는 그냥...돌자
            if arr[j] < arr[j - 1]:  # 다음거보다 지금이 작으면
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # 바꿔준다

    sorted_arr = []
    # 앞 다섯개는 최소, 뒤 다섯개는 최대
    for k in range(5):
        sorted_arr.append(arr[-k - 1])  # 큰거
        sorted_arr.append(arr[k])  # 작은거
    return sorted_arr


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())  # 정수의 갯수
    nums = list(map(int, input().split()))  # 정수 리스트

    # 정렬 후 앞 10개를 반환하는 함수를 시행한다.
    sorted_nums = specific_sort(nums, N)

    print(f'#{tc}', *sorted_nums)
~~~
<br><br>


# 총평
- "앞 5개 최소값, 뒤 5개 최대값"을 번갈아 출력하는 요구사항을 잘 구현했습니다.
- 버블정렬을 두 번 수행하는 방식은 동작은 맞지만, 내림차순 부분은 사실 필요 없이 전체 정렬 후 슬라이싱으로 구현 가능해 코드가 단순해질 수 있습니다.
- 현재 방식은 부분 버블정렬을 두 번 사용하여 O(N×5) 정도로 동작하지만, 전체 길이가 길어도 큰 차이는 없습니다.
- 다만 현재 구현은 원본 배열을 직접 수정하므로, 원본 보존이 필요하면 복사본을 사용해야 합니다.

<br><br>


# 보완점
## 1. 불필요한 두 번째 버블정렬 제거
이미 첫 버블정렬에서 최소 5개 원소는 확정되므로, 최대 5개 원소는 `max()`를 반복하거나 전체 정렬 후 인덱싱으로 바로 뽑아낼 수 있습니다.
~~~python
arr_sorted = sorted(arr)
result = []
for k in range(5):
    result.append(arr_sorted[-(k+1)])  # 큰 값
    result.append(arr_sorted[k])       # 작은 값
~~~

<br><br>


## 2. 내장 정렬 사용으로 간결화
버블정렬은 학습 목적 외에는 비효율적입니다. 내장 `sorted()`는 O(N log N)이며, 코드 길이와 가독성이 크게 개선됩니다.
~~~python
def specific_sort(arr):
    arr_sorted = sorted(arr)
    result = []
    for k in range(5):
        result.append(arr_sorted[-(k+1)])
        result.append(arr_sorted[k])
    return result
~~~

<br><br>


# 최종 코드 예시
~~~python
# [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
# 내장 정렬 + 슬라이싱으로 간결하게

import sys

def specific_sort(arr):
    """정렬 후 최대/최소를 번갈아 10개 추출"""
    arr_sorted = sorted(arr)
    result = []
    for k in range(5):
        result.append(arr_sorted[-(k+1)])  # 큰 값
        result.append(arr_sorted[k])       # 작은 값
    return result

def main():
    input = sys.stdin.readline
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        nums = list(map(int, input().split()))
        sorted_nums = specific_sort(nums)
        print(f"#{tc}", *sorted_nums)

if __name__ == "__main__":
    main()
~~~
