- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 주석/변수 최소화](#1-불필요한-주석변수-최소화)
  - [2. 결과 문자열 반환 기능 추가 가능](#2-결과-문자열-반환-기능-추가-가능)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = input()         # 문자열 입력
    stack = []          # stack 초기화

    # 문자열을 순회하며
    for char in chars:
        if stack and stack[-1] == char:     # stack이 비어있지 않으며 마지막값이 지금 값과 같다면
            stack.pop()     # pop 하기
        else:
            stack.append(char)      # 아니라면 원소를 추가

    print(f'#{tc} {len(stack)}')   # 남은 stack 길이 출력
~~~
<br><br>


# 총평
- 스택을 활용한 **연속 중복 문자 제거** 알고리즘이 잘 구현되어 있습니다.
- `if stack and stack[-1] == char:` 조건으로 스택 비어있을 때의 예외를 방지한 점이 깔끔합니다.
- 시간 복잡도는 O(N)이며, 입력 문자열 길이가 커도 효율적입니다.
- 이 문제에서는 길이 출력이 목표지만, 필요 시 `''.join(stack)`을 사용하면 최종 문자열도 구할 수 있습니다.
<br><br>


# 보완점
## 1. 불필요한 주석/변수 최소화
- 스택의 초기화, 순회 등의 주석은 코드 자체가 직관적이므로 간결화 가능.
- `stack`을 리스트 그대로 사용해도 좋지만, collections.deque를 사용하면 pop/append가 더 빠릅니다(여기서는 미미한 차이).
~~~python
from collections import deque

stack = deque()
for char in chars:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
~~~

<br><br>


## 2. 결과 문자열 반환 기능 추가 가능
- 문제 변형에서 최종 문자열을 출력하거나 활용할 수 있도록 함수화.
~~~python
def remove_adjacent_duplicates(s: str) -> str:
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)
~~~


<br><br>


# 최종 코드 예시
~~~python
# 4873. 반복문자 지우기

def remove_adjacent_duplicates_length(s: str) -> int:
    """
    연속된 같은 문자를 제거한 뒤 남은 문자열의 길이 반환.
    """
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        chars = input().strip()
        print(f'#{tc} {remove_adjacent_duplicates_length(chars)}')

if __name__ == "__main__":
    main()
~~~
