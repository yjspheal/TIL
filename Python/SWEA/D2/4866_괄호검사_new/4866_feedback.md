- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 코드 간소화](#1-코드-간소화)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

# import sys
#
# sys.stdin = open('sample_input.txt')


def check_valid_bracket(chars):
    """
    chars에서 중괄호, 소괄호가 제대로 짝을 이뤘는지 검사하는 함수
    Args:
        chars (str): 한 줄의 문자열
    Returns:
        boolean:  정상 -> True, 비정상 -> False
    """
    stack = []  # stack 초기화
    open_bracket_set = ('(', '{')
    close_bracket_set = (')', '}')
    bracket_dict = {')': '(', '}': '{'}  # 닫는 괄호 : 여는 괄호만 있으면 됨

    # chars를 순회하며
    for char in chars:
        if char in open_bracket_set:  # 여는 괄호면 push
            stack.append(char)
        elif char in close_bracket_set:  # 닫는 괄호면
            if not stack:  # 근데 스택이 비어있으면
                return False  # 비정상

            last_bracket = stack.pop()  # 스택의 마지막값이
            if last_bracket != bracket_dict[char]:  # 닫는 괄호(char)와 매치되는 여는 괄호가 아니라면
                return False  # 비정상

    # 다 돌았는데 stack이 남아있다면 비정상, 안남아있다면 정상을 return
    return False if stack else True


T = int(input())
for tc in range(1, T + 1):
    sentence = input()      # 한 줄의 문자열 입력
    result = 1 if check_valid_bracket(sentence) else 0    # 괄호 맞는지 체크, True면 1 False면 0으로 변경

    print(f'#{tc} {result}')
~~~
<br><br>


# 총평
- 스택을 이용해 여는 괄호 push, 닫는 괄호 pop & 매칭 확인하는 전형적인 괄호검사 알고리즘이 잘 구현되었습니다.
- `bracket_dict`를 이용해 매칭 괄호를 딕셔너리로 관리하는 방식이 명확합니다.
- 불필요한 괄호나 다른 문자들을 자연스럽게 무시하고, 소괄호·중괄호 모두 지원합니다.
- `return False if stack else True` 대신 `return not stack`로 더 간결하게 표현 가능.
<br><br>


# 보완점
## 1. 코드 간소화
- 여는/닫는 괄호 집합은 사실 `bracket_dict.values()`와 `bracket_dict.keys()`로도 얻을 수 있으므로 중복 선언이 불필요합니다.
- 마지막에 스택 비어있는지 여부는 `return not stack`으로 표현.
~~~python
bracket_dict = {')': '(', '}': '{'}
for char in chars:
    if char in bracket_dict.values():
        stack.append(char)
    elif char in bracket_dict:
        if not stack or stack.pop() != bracket_dict[char]:
            return False
return not stack
~~~

<br><br>




# 최종 코드 예시
~~~python
# 4866. 괄호검사

from typing import Dict

def check_valid_bracket(chars: str) -> bool:
    """
    문자열에서 괄호 짝이 올바른지 검사.
    지원: (), {}, [], <>
    """
    bracket_dict: Dict[str, str] = {')': '(', '}': '{', ']': '[', '>': '<'}
    stack = []
    for char in chars:
        if char in bracket_dict.values():  # 여는 괄호
            stack.append(char)
        elif char in bracket_dict:         # 닫는 괄호
            if not stack or stack.pop() != bracket_dict[char]:
                return False
    return not stack

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        sentence = input().strip()
        result = int(check_valid_bracket(sentence))
        print(f'#{tc} {result}')

if __name__ == "__main__":
    main()
~~~
