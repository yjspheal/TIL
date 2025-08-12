- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. `collections.Counter`로 간결하고 안전하게](#1-collectionscounter로-간결하고-안전하게)
  - [2. 함수화 및 main 가드로 테스트 용이성 향상](#2-함수화-및-main-가드로-테스트-용이성-향상)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# [파이썬 S/W 문제해결 기본] 3일차 - 글자수

# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = set(input())     # 길이가 N인 문자열 1, 1개씩만 있으면 되므로 set처리
    str2 = input()          # 길이가 M인 문자열 2


    # str2에 들어있는 문자별 갯수를 저장할 dict 초기화
    char_dict = {}
    
    max_count = 0   # 제일 큰 횟수 저장

    for char in str2:   # str2에 있는 문자가
        if char in str1:        # str1에도 있다면
            # dict의 value에 +1을 해준다. 만약 없었다면 0 + 1 = 1을 넣는다.
            char_dict[char] = char_dict.get(char, 0) + 1

            if char_dict[char] > max_count:     # max값을 넘겼다면
                max_count = char_dict[char]     # update
    
    print(f'#{test_case} {max_count}')
~~~
<br><br>


# 총평
- 문제 의도를 정확히 반영한 정답 코드입니다. `str1`을 `set`으로 만들어 membership 테스트를 O(1)로 만든 점이 효율적입니다.
- 한 번의 선형 순회로 카운팅과 동시 최대값 갱신을 해 O(M) 시간에 해결합니다.
- 다만 표준 라이브러리(`collections.Counter`)를 사용하면 의도가 더 분명해지고 코드가 간결해집니다.
- 입출력/구조(함수화, main 가드) 정리로 재사용성과 테스트 편의성이 좋아질 수 있습니다.

<br><br>


# 보완점
## 1. `collections.Counter`로 간결하고 안전하게
`Counter`로 `str2` 전체 빈도를 한 번에 계산한 뒤, `str1`에 존재하는 문자만 최대값을 구하면 로직이 더 짧고 명확합니다. 교집합이 없을 때를 대비해 `max(..., default=0)`로 안전하게 처리합니다.
~~~python
from collections import Counter

cnt = Counter(str2)
max_count = max((cnt[ch] for ch in str1), default=0)
~~~

<br><br>


## 2. 함수화 및 main 가드로 테스트 용이성 향상
문제 풀이 코드를 함수로 감싸면 별도 테스트(예: 단위 테스트, 샘플 입력) 시 재사용이 쉽습니다. 또한 `if __name__ == "__main__":` 가드를 두면 모듈 임포트 시 실행을 방지할 수 있습니다.
~~~python
def solve_one(s1: str, s2: str) -> int:
    from collections import Counter
    target = set(s1)
    cnt = Counter(s2)
    return max((cnt[ch] for ch in target), default=0)
~~~

<br><br>


# 최종 코드 예시
~~~python
# [파이썬 S/W 문제해결 기본] 3일차 - 글자수
# 표준 풀이: Counter + set, O(M) 시간

from collections import Counter
import sys

def solve_one(s1: str, s2: str) -> int:
    """s1의 문자들 중 s2에서 가장 많이 등장하는 문자의 빈도를 반환."""
    target = set(s1)                 # membership O(1)
    cnt = Counter(s2)                # s2 전체 빈도 계산
    return max((cnt[ch] for ch in target), default=0)  # 교집합 없으면 0

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        s1 = input().strip()
        s2 = input().strip()
        ans = solve_one(s1, s2)
        print(f"#{tc} {ans}")

if __name__ == "__main__":
    main()
~~~
