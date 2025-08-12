- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 매핑 딕셔너리 초기화 간결화](#1-매핑-딕셔너리-초기화-간결화)
  - [2. 문자열 누적 대신 join 사용](#2-문자열-누적-대신-join-사용)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
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
~~~
<br><br>


# 총평
- 카운팅 정렬 원리를 잘 적용했고, 외계어→숫자 매핑과 역변환을 깔끔하게 구현했습니다.
- 딕셔너리 초기화 부분을 `enumerate`로 간결하게 표현할 수 있습니다.
- 문자열 누적(`result += ...`)은 반복이 많을 경우 비효율적이므로 리스트에 append 후 `' '.join()`을 쓰면 성능이 개선됩니다.
- 입력에서 외계어 리스트를 문자열로 한 번에 받는 대신 `split()` 처리하여 리스트 상태로 바로 전달하면 불필요한 split 반복을 줄일 수 있습니다.

<br><br>


# 보완점
## 1. 매핑 딕셔너리 초기화 간결화
현재는 `for i in range(10)`으로 생성하지만, `enumerate`를 쓰면 더 직관적입니다.
~~~python
alien_earth_dict = {word: idx for idx, word in enumerate(alien_list)}
~~~

<br><br>


## 2. 문자열 누적 대신 join 사용
문자열은 불변(immutable)이므로 `+=` 반복은 새로운 문자열을 계속 생성합니다. 리스트에 append 후 join하면 더 효율적입니다.
~~~python
result_parts = []
for k in range(10):
    result_parts.extend([alien_list[k]] * counts[k])
return ' '.join(result_parts)
~~~

<br><br>


# 최종 코드 예시
~~~python
# 1221. [S/W 문제해결 기본] 5일차 - GNS
# 카운팅 정렬 + join 방식으로 성능 개선

import sys

def sort_alien_number(alien_words):
    """외계어 숫자들을 카운팅 정렬하여 반환"""
    alien_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    alien_earth_dict = {word: idx for idx, word in enumerate(alien_list)}
    
    counts = [0] * 10
    for alien_num in alien_words:
        counts[alien_earth_dict[alien_num]] += 1
    
    result_parts = []
    for k in range(10):
        result_parts.extend([alien_list[k]] * counts[k])
    
    return ' '.join(result_parts)

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(1, T + 1):
        tc, N = input().split()
        N = int(N)
        alien_sentence = input().split()
        
        sorted_alien_sentence = sort_alien_number(alien_sentence)
        
        print(tc)
        print(sorted_alien_sentence)

if __name__ == "__main__":
    main()
~~~
