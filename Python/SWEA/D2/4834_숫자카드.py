# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드


# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    card_strs = input()  # 각 카드가 공백없이 문자열로 들어옴

    card_count = [0] * 10       # 카드 갯수 저장할 10개짜리 리스트

    for card_str in card_strs:
        card_count[int(card_str)] += 1  # 카드 한장마다 추가
    

    max_card_count = max(card_count)  # 가장 많은 장수를 찾아냄


    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다. 는 조건이 있으므로 뒤집음
    card_count = card_count[::-1]  

    # 가장 많은 장수가 있는 카드를 찾아냄
    inverse_max_card_num = card_count.index(max_card_count) 

    max_card_num = 9 - inverse_max_card_num  # 되돌리기


    
    print(f'#{test_case} {max_card_num} {max_card_count}')
