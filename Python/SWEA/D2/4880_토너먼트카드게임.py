# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
 
# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    
    # dp[l][r]에 단순 우승자가 아니라,
    # [l…r] 구간에서 진행된 모든 매치 승리 로그를 리스트로 저장
    dp = [[None]*(N+1) for _ in range(N+1)]
    
    # 길이 1 구간: 자기 자신이 유일한 로그
    for i in range(1, N+1):
        dp[i][i] = [i]   # 리스트에 학생 번호 하나만

    # 길이 2부터 N까지 모든 구간 처리
    for length in range(2, N+1):
        for l in range(1, N-length+2):
            r = l + length - 1
            mid = (l + r)//2
            
            left_log  = dp[l][mid]       # e.g. [a, b, c, ...]
            right_log = dp[mid+1][r]     # e.g. [x, y, z, ...]
            
            left_winner  = left_log[-1]   # 구간 [l…mid]의 마지막 승자
            right_winner = right_log[-1]  # 구간 [mid+1…r]의 마지막 승자
            
            lc = cards[left_winner-1]
            rc = cards[right_winner-1]
            
            # 카드 비교
            if lc == rc:
                winner = left_winner if left_winner < right_winner else right_winner
            elif (lc==1 and rc==3) or (lc==2 and rc==1) or (lc==3 and rc==2):
                winner = left_winner
            else:
                winner = right_winner
            
            # **중요**: 매치 로그를 전부 이어 붙이고 마지막에 새 승자 추가
            # → O(length) 리스트 병합, 전체적으로 O(N³) 메모리/시간
            dp[l][r] = left_log + right_log + [winner]
    
    # 최종 구간 [1…N]의 로그
    final_log = dp[1][N]
    # 마지막에 기록된 값이 “최종 우승자”
    champion = final_log[-1]

    print(f"#{tc} {champion}")
