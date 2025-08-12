- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. `len_arr` 제거 및 `len()` 사용](#1-len_arr-제거-및-len-사용)
  - [2. 내장 정렬을 활용한 간결화](#2-내장-정렬을-활용한-간결화)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 4843_특별한정렬. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

def specific_sort(arr, len_arr):
    """
    정수로 이루어진 리스트를 인자로 받아, 가장 큰 수 - 가장 작은 수 - 그다음 큰 수 - 그다음 작은 수 ...로 정렬하여 return
    단, 앞의 10개 즉 큰수 5개 / 작은 수 5개만 정렬한다.

    Args:
        arr (list): 정수로 이루어진 리스트. 정렬 전 원본
        len_arr (int): arr 길이

    Returns:
        list: 정렬된 arr의 앞 10개만 담은 list
    """

    # 선택 정렬을 위한 idx 추출

    for i in range(10):
        # 이번에 찾을 최대 or 최소의 인덱스와 값을 초기화
        target_idx = i
        target_value = arr[i]

        if i % 2 == 0:  # 짝수번째 인덱스라면 큰 수가 위치해야함
            for j in range(i, len_arr):
                if arr[j] > target_value:
                    target_value = arr[j]
                    target_idx = j

        else:  # 홀수번째 인덱스라면 작은 수가 위치해야함
            for j in range(i, len_arr):
                if arr[j] < target_value:
                    target_value = arr[j]
                    target_idx = j

        # 한번 다 돌고나면 최대 or 최소 idx가 나온다.
        # 자리를 바꿔주자
        arr[target_idx], arr[i] = arr[i], arr[target_idx]

    # 열 번이 돌고나면 앞에 10개가 정렬되어있다.
    return arr[:10]


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
- 문제 요구사항(큰 수와 작은 수를 번갈아 5쌍 = 10개 출력)을 정확하게 구현했습니다.
- 선택정렬 방식으로 부분 정렬을 수행하므로 전체 정렬보다 효율적이며, O(10×N) ≈ O(N)입니다.
- 다만 `len_arr` 매개변수는 사실 `len(arr)`로 바로 구할 수 있으므로 인자로 받을 필요가 없습니다.
- 코드 구조는 명확하지만, 같은 로직을 내장 정렬과 슬라이싱으로 더 간단하게 구현할 수도 있습니다.
- 원본 리스트를 직접 수정하므로, 원본 보존이 필요하면 복사본을 사용하는 것이 좋습니다.

<br><br>


# 보완점
## 1. `len_arr` 제거 및 `len()` 사용
`len_arr`는 함수 호출 시 중복 계산된 값입니다. 함수 내부에서 `len(arr)`를 쓰면 더 깔끔합니다.
~~~python
def specific_sort(arr):
    n = len(arr)
    ...
~~~

<br><br>


## 2. 내장 정렬을 활용한 간결화
선택정렬 학습 목적이 아니라면 `sorted()`로 전체 정렬 후 인덱싱으로 원하는 형태를 쉽게 만들 수 있습니다.
~~~python
def specific_sort(arr):
    arr_sorted = sorted(arr, reverse=True)  # 내림차순
    result = []
    for i in range(5):
        result.append(arr_sorted[i])        # 큰 수
        result.append(arr_sorted[-(i+1)])   # 작은 수
    return result
~~~

<br><br>


# 최종 코드 예시
~~~python
# 4843_특별한정렬 - 내장 정렬 버전

def specific_sort(arr):
    """큰 수-작은 수 번갈아 10개 추출"""
    arr_sorted = sorted(arr)
    result = []
    for i in range(5):
        result.append(arr_sorted[-(i+1)])  # 큰 값
        result.append(arr_sorted[i])       # 작은 값
    return result

def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        nums = list(map(int, input().split()))
        sorted_nums = specific_sort(nums)
        print(f"#{tc}", *sorted_nums)

if __name__ == "__main__":
    main()
~~~
