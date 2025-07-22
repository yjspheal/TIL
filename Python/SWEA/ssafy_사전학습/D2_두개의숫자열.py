
'''import sys
sys.stdin = open("input.txt", "r")


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

⚠️ 개선점
1. 불필요한 0 padding
python
코드 복사
Ai = Ai + [0]*(M - N)  # 둘이 길이 맞춤
→ 이건 실제 문제의 요구사항에 맞지 않습니다. 내적 비교를 위해 짧은 쪽을 슬라이딩 시켜야지, 길이를 맞출 필요는 없습니다. 이 때문에 뒤에서 Ai를 pop하고 다시 넣는 코드가 꼬입니다.

2. 슬라이딩 방향이 역방향
python
코드 복사
Ai = [Ai.pop()] + Ai
→ 리스트 끝의 원소를 앞으로 보내는 방식인데, 일반적으로 슬라이딩 윈도우는 앞에서부터 슬라이딩하면서 비교합니다. 이 부분이 직관적이지 않고 비효율적입니다.

3. 불필요한 NumPy
단순히 리스트 간의 곱과 합만 필요한 경우라면 굳이 numpy를 사용할 필요는 없습니다. 작은 데이터에서는 오히려 느릴 수도 있습니다.


'''

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 항상 Ai가 더 짧게 만듦
    if N > M:
        Ai, Bj = Bj, Ai
        N, M = M, N

    max_sum = -float('inf')
    for i in range(M - N + 1):
        total = sum([Ai[j] * Bj[i + j] for j in range(N)])
        max_sum = max(max_sum, total)

    print(f"#{test_case} {max_sum}")
