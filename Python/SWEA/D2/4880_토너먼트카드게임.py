# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# dict{(학생번호, 카드번호) = round depth}

# [(학생번호, 카드번호), (학생번호, 카드번호), 1, ]
for test_case in range(1, T + 1):
    N = int(input())    # 학생 수

    # 카드 번호 list로 input
    cards = map(int, input().split())

    rcp_dict = {}
    for i in range(N):
        rcp_dict[(i, cards[i])] = 0     # 마지막 라운드가 될 값을 0으로 설정

    







    
    print(f'#{test_case} ')