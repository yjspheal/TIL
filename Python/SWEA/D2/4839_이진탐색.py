# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")



def binary_search(l, r, target):
    """
    주어진 범위 [l, r]에서 이진 탐색의 한 단계를 실행하여,
    목표값이 포함된 절반 범위 혹은 검색 종료 신호를 반환합니다.

    Args:
        l (int): 탐색 범위의 하한값.
        r (int): 탐색 범위의 상한값.
        target (int): 찾고자 하는 목표값.

    Returns:
        Union[str, tuple]:
            - 'end': 중간값이 target과 일치하여 탐색이 완료된 경우.
            - (new_l, new_r, target): 중간값과 일치하지 않아 범위를 절반으로 좁힌 후의
              하한 new_l, 상한 new_r, 그리고 여전히 탐색 대상인 target을 튜플로 반환.

    Examples:
        >>> # 범위 [1, 9], target=5
        >>> binary_search(1, 9, 5)
        (5, 9, 5)      # 1) 중간값 c=5, c==target이므로 'end' 반환
        'end'
        
        >>> # 범위 [1, 9], target=8
        >>> binary_search(1, 9, 8)
        (5, 9, 8)      # c=5, target>5 이므로 new_l=5, new_r=9 반환
        
        >>> # 범위 [1, 9], target=3
        >>> binary_search(1, 9, 3)
        (1, 5, 3)      # c=5, target<5 이므로 new_l=1, new_r=5 반환

    Note:
        - 이 함수는 전체 탐색을 수행하지 않고, 단 한 단계만 분할하여 결과를 돌려줍니다.
        - 반복적 호출을 통해 전체 범위를 좁혀가며 사용하세요.
    """

    c = int((l + r) / 2) # 기준이 될 중간 페이지

    # 정확히 target이 된 시점
    if c == target:
        return 'end'
    
    else:
        if target > c:      # target이 절반값보다 크다면 l을 업데이트
            l = c
        else:               # target이 절반값보다 작다면 r을 업데이트
            r = c
    
    return l, r, target     # 매개변수 순서대로 다시 return

def count_search(pages, target):
    """
    총 페이지 수가 pages인 책에서 target 페이지를 찾기 위해
    몇 번의 binary_search 호출이 필요한지 계산하여 반환합니다.

    Args:
        pages (int): 책의 총 페이지 수. (1 이상의 정수)
        target (int): 찾고자 하는 페이지 번호. (1 이상 pages 이하의 정수)

    Returns:
        int: target 페이지를 찾기 위해 실행된 binary_search 호출 횟수.

    Raises:
        ValueError: 
            - pages가 1보다 작은 경우
            - target이 1보다 작거나 pages보다 큰 경우


    Note:
        - binary_search 함수는 한 단계마다 탐색 범위를 절반으로 줄입니다.
    """


    search_result = (1, pages, target)     # 맨 처음 탐색값으로 초기화
    search_count = 0
    
    while search_result != 'end':       # end가 아닌 동안 계속 루프
        search_result = binary_search(*search_result)    # 이진탐색을 위한 range 업데이트

        search_count += 1       # 탐색 횟수 + 1

    return search_count



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    pages, target_A, target_B = map(int, input().split())   

    # 각 search 횟수 계산
    search_count_A = count_search(pages, target_A)
    search_count_B = count_search(pages, target_B)
    
    # 승자 계산
    if search_count_A < search_count_B:
        winner = 'A'
                
    elif search_count_A > search_count_B:
        winner = 'B'

    else:       # 비김
        winner = 0


    print(f'#{test_case} {winner}')