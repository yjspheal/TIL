# import sys
#
# sys.stdin = open('input.txt')

def bubble_sort(arr):
    """
    arr를 순회하며 인접한 원소의 크기를 비교, 오름차순으로 정렬하여 반환하는 함수

    Args:
        arr (list): 원본 리스트

    Returns:
        List: 정렬된 리스트
    """

    # arr 길이
    n = len(arr)

    # i는 n-1부터 1까지
    for i in range(n-1, 0, -1):
        # j는 i 전까지(인접 2개를 ㅂ교해야 하므로)
        for j in range(0, i):
            # 다음 원소랑 비교했을 때 뒤집어야 된다면
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap

    return arr

numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)