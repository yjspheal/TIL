# 1221. [S/W 문제해결 기본] 5일차 - GNS

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
import sys

sys.stdin = open("GNS_test_input.txt", "r")


def sort_alien_number(alien_strs):
    """
    외계어 숫자들을 표현하는 문자열을 카운팅 정렬하여 오름차순으로 return
    Args:
        alien_strs (str): 외계어 숫자 문자열
    Returns:
        str: 정렬된 alien_strs
    """

    # 외계어 해석을 위한 딕셔너리 생성
    alien_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    alien_earth_dict = {}
    for i in range(10):
        alien_earth_dict[alien_list[i]] = i
    # alien_earth_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    # 정렬을 위해 갯수를 세는 리스트 생성
    counts = [0] * 10

    for alien_num in alien_strs.split():
        earth_num = alien_earth_dict[alien_num]     # 지구숫자로 변환
        counts[earth_num] += 1                # 해당 숫자 부분에 count +1

    # 문자열에 정렬된 결과 붙이기
    result = ''
    for k in range(10):
        for _ in range(counts[k]):
            result += alien_list[k] + ' '

    return result.strip()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    tc, N = map(str, input().split())     # 테케 번호와 외계숫자 수
    N = int(N)

    alien_sentence = input()        # 외계어 input

    sorted_alien_sentence = sort_alien_number(alien_sentence)       # 정렬

    print(f'{tc}')
    print(sorted_alien_sentence)

