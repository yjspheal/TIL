# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")

# import copy

# def remove_arr_line(arr, col, row):
#     """
#     어떤 arr와 x, y 좌표가 들어오면, 해당 라인을 제거한 new_arr를 return하는 함수

#     Args:
#         arr (list): 어떤 행렬
#         col (int): 제거할 열, 즉 x값
#         row (int): 제거할 행, 즉 y값
    
#     Return:
#         List : arr에서 x, y 라인 제거한 새로운 arr
#     """

#     # 행 삭제
#     arr = arr.remove(row)

#     # 열 삭제
#     for r in arr:
#         del r[col]

#     return arr


# def search_min_sum(arr, n):
#     global min_sum
#     """
#     NxN 행렬 arr에 대해, 한줄에 하나씩 숫자를 골라 최소합을 구하여 return하는 함수
#     단, 세로줄에서도 하나만을 골라야 함.

#     Args:
#         arr (list): nxn 행렬
#         n (int): n

#     Returns:
#         int: 가로줄 세로줄 겹치지 않는 최소합
#     """

#     arr_rm = copy.deepcopy(arr)
    
#     # 첫줄에서 원소 하나씩 순회하며 
#     for x in range(n):
#         current_sum = 0
#         for j in range(n):
#             arr_rm = remove_arr_line(arr_rm)
#             new_n = len(arr_rm)
#             if new_n == 1:     # 다 없어져 원소가 하나만 남았다면
#                 return arr, arr_rm[0][0]
#             else:
#                 return search_min_sum(arr_rm, new_n)





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())

    matrix = [] # NxN행렬을 저장할 리스트
    # N줄에 걸쳐 10보다 작은 자연수가 주어짐
    for _ in range(N):
        row = list(map(int, input().split()))

    #     # 모든 줄을 matrix에 추가
    #     matrix.append(row)

    # # 최소합의 초기값을 sum(diagonal)로 set
    # min_sum = sum(matrix[i][i] for i in range(N))

    # # 최소합 계산
    # result = search_min_sum(matrix, N)
        
    # 출력
    print(f'#{tc} ')