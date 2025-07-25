# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    target = input()        # 길이 N의 문자열
    base  = input()         # 길이 M의 문자열

    # target이 base에 있었는지 여부
    isin_base = 0

    idx = 0
    len_target = len(target)    # N
    len_base = len(base)        # M

    while idx <= len_base - len_target:

        if base[idx] == target[0]:      # 시작 문자가 같다면
            if base[idx:(idx + len_target)] == target:  # 그래서 아예 같은 문자열이라면
                isin_base = 1       # 1을 만들고 break
                break

        # 위 과정 후 idx += 1
        idx += 1
    
    print(f'#{test_case} {isin_base}')