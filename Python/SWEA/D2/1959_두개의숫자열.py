# 1959. 두 개의 숫자열

# import sys
# sys.stdin = open("input.txt", "r")


import numpy as np

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))


    if N > M:
        N, M = M, N
        Ai, Bj = Bj, Ai


    Ai = Ai + [0]*(M - N) # 둘이 길이 맞춤
    
    max_multsum = 0

    for time in range(M-N+1):
        Ai_arr = np.array(Ai)
        Bj_arr = np.array(Bj)

        multsum = sum(Ai_arr * Bj_arr)
        # print(Ai_arr, Bj_arr, multsum)
        max_multsum = max(multsum, max_multsum)

        Ai = [Ai.pop()] + Ai
    print(f"#{test_case} {max_multsum}")

