- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 변수 제거](#1-불필요한-변수-제거)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 1989_초심자의회문검사

import sys
sys.stdin = open("input.txt")

T = int(input())    # 테케 갯수 입력
for tc in range(1, T+1):
    sentence = input()  # 문자열 입력

    if sentence == sentence[::-1]:   # 뒤집은 것이 원본과 똑같다면
        is_palindrome = 1           # 회문임
    else:
        is_palindrome = 0           # 다르다면 회문 아님

    print(f"#{tc} {is_palindrome}")
~~~
<br><br>


# 총평
- 코드가 직관적이며, 파이썬의 슬라이싱을 잘 활용해 회문 여부를 간단히 검사함.
- 가독성이 높으나, 불필요한 `if-else` 구조를 줄여 더 간결하게 만들 수 있음.
- `sys.stdin` 사용은 로컬 테스트에는 좋으나, 제출 환경에서는 불필요할 수 있음.
- 불필요한 변수(`is_palindrome`) 없이 바로 출력 가능.

<br><br>


# 보완점
## 1. 불필요한 변수 제거
- `is_palindrome` 변수를 만들지 않고, 조건식에서 바로 정수형으로 변환하여 출력 가능.
~~~python
print(f"#{tc} {int(sentence == sentence[::-1])}")
~~~

<br><br>


# 최종 코드 예시
~~~python
# 1989_초심자의회문검사

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T+1):
    sentence = input()
    print(f"#{tc} {int(sentence == sentence[::-1])}")
~~~
