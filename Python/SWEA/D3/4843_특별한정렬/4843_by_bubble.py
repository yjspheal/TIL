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
