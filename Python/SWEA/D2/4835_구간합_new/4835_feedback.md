- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 슬라이딩 윈도우로 시간복잡도 개선](#1-슬라이딩-윈도우로-시간복잡도-개선)
  - [2. 내장 sum() 사용 및 함수 제거](#2-내장-sum-사용-및-함수-제거)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

import sys

sys.stdin = open("sample_input.txt", "r")


def sum_list(arr):
    """
    주어진 리스트의 모든 원소를 합하여 return 하는 함수

    Args:
        arr (list): 주어진 리스트

    Returns:
        int: 모든 원소의 합

    Notes:
        arr 의 모든 원소는 정수로 이루어져있다
    """

    # 반환할 합의 값
    result = 0

    for num in arr:
        result += num

    return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 정수의 갯수 _와, 합칠 구간의 갯수 section_length
    _, section_length = map(int, input().split())

    digit_list = list(map(int, input().split()))

    # 최대 최소값 초기화 = 맨 처음 구간합
    min_sum = max_sum = sum_list(digit_list[:section_length])

    # 모든 구간을 순회하며 sum 값을 업데이트
    for i in range(len(digit_list) - section_length + 1):
        current_sum = sum_list(digit_list[i:(i + section_length)])

        if current_sum > max_sum:  # current가 max_sum을 넘겼다면
            max_sum = current_sum
        if current_sum < min_sum:  # current가 min_sum보다 작다면
            min_sum = current_sum

    print(f'#{test_case} {max_sum - min_sum}')
~~~
<br><br>


# 총평
- 구간합을 정확히 계산하는 정답 코드이며, `sum_list` 함수로 합산 기능을 분리해 가독성이 좋습니다.
- 다만 매 구간마다 `sum_list`를 호출하는 방식은 O(N×K)로 비효율적입니다(K는 구간 길이).
- 슬라이딩 윈도우 기법을 적용하면 O(N)으로 성능이 개선됩니다.
- Python 내장 `sum()`을 사용하면 별도의 합산 함수 없이 간결하게 작성 가능합니다.
- 첫 번째 구간합을 초기화한 후, 한 칸씩 이동하며 갱신하는 로직이 있으면 메모리 접근량이 줄어듭니다.

<br><br>


# 보완점
## 1. 슬라이딩 윈도우로 시간복잡도 개선
현재는 구간마다 `sum_list`를 호출해 중복 계산이 많습니다. 첫 구간합을 계산한 뒤, 이동 시 앞 원소를 빼고 뒤 원소를 더하는 방식으로 O(1) 갱신이 가능합니다.
~~~python
current_sum = sum(digit_list[:section_length])
min_sum = max_sum = current_sum

for i in range(section_length, len(digit_list)):
    current_sum += digit_list[i] - digit_list[i - section_length]
    min_sum = min(min_sum, current_sum)
    max_sum = max(max_sum, current_sum)
~~~

<br><br>


## 2. 내장 sum() 사용 및 함수 제거
`sum_list`는 학습 목적 외에는 불필요하며, 내장 `sum()`이 C로 구현돼 더 빠릅니다.
~~~python
min_sum = max_sum = sum(digit_list[:section_length])
~~~

<br><br>


# 최종 코드 예시
~~~python
# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
# 슬라이딩 윈도우 방식 O(N) 구현

import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for test_case in range(1, T + 1):
        _, section_length = map(int, input().split())
        digit_list = list(map(int, input().split()))
        
        # 초기 구간합
        current_sum = sum(digit_list[:section_length])
        min_sum = max_sum = current_sum
        
        # 윈도우 이동하며 합 갱신
        for i in range(section_length, len(digit_list)):
            current_sum += digit_list[i] - digit_list[i - section_length]
            min_sum = min(min_sum, current_sum)
            max_sum = max(max_sum, current_sum)
        
        print(f"#{test_case} {max_sum - min_sum}")

if __name__ == "__main__":
    main()
~~~
