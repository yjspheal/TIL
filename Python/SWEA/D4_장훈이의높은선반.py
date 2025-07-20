# by gpt

def solve_case(N, B, heights):
    min_over = float('inf')  # B 이상 중 가장 작은 합

    for i in range(1, 1 << N):  # 1부터 시작해서 공집합 제외
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += heights[j]
        if total >= B:
            min_over = min(min_over, total)
    
    return min_over - B


# 입력 처리
T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = solve_case(N, B, heights)
    print(f"#{t} {result}")
