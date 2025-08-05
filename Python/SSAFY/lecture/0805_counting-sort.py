def counting_sort(input_arr, k):
    """
    input_arr를 k(input_arr 속 가장 큰 정수 + 1)를 이용하여 카운팅정렬하여 return 하는 함수

    Args:
        input_arr (list): 정렬할 원본 리스트
        k (int): input_arr 속 가장 큰 정수 + 1

    Returns:
        List: 정렬된 리스트
    """
    # input_arr 의 각 원소별 갯수를 저장할 list
    counts = [0] * k

    # input_arr를 순회하며 각 원소의 갯수를 counts 에 업데이트
    for num in input_arr:
        counts[num] += 1

    # counts 의 각 원소값을 counts[i] += counts[i-1] <- 인덱스를 찾기 위해
    for i in range(1, k):
        counts[i] += counts[i - 1]

    sorted_list = [0] * len(input_arr)   # return 할 리스트

    # input_arr 가 존재하는동안
    while input_arr:
        # arr 의 마지막 원소부터 탐색하며, sorted_list 에 추가
        ele = input_arr.pop()     # 마지막 원소
        idx = counts[ele] - 1   # ele 위치에 있는 값은 sorted_list 에 몇번째로 들어가야하는지를 나타내므로
        counts[ele] -= 1        # 갯수 하나 썼으므로 -1

        sorted_list[idx] = ele      # 넣기

    return sorted_list

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]
