
- [총평](#총평)
- [보완점](#보완점)
  - [1. 스택 이용한 O(n) 유효성 검사](#1-스택-이용한-on-유효성-검사)
  - [2. 괄호 필터링 간결화](#2-괄호-필터링-간결화)
  - [3. 함수화 및 입력 로직 분리](#3-함수화-및-입력-로직-분리)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 입력 문자열에서 괄호 문자만 추출하여 검증 로직에 사용하는 접근이 적절함
- `replace`를 반복 적용하여 괄호 쌍을 제거하는 방식이 동작하지만, 반복문 내 `replace`가 매 반복마다 문자열을 스캔해 비효율적임
- 예외 케이스(비정상 괄호 순서) 검출 시 조기 종료를 구현한 점은 좋음

<br>

# 보완점
## 1. 스택 이용한 O(n) 유효성 검사
이중 `replace` 루프 대신 단일 스캔으로 괄호 짝을 검증하는 스택 알고리즘으로 변경하세요.
```python
def is_valid_brackets(s):
    stack = []
    pairs = {')':'(', '}':'{'}
    for ch in s:
        if ch in '({':
            stack.append(ch)
        elif ch in ')}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```  

<br>

## 2. 괄호 필터링 간결화
현재 반복문으로 필터링하는 대신 리스트 컴프리헨션으로 간결하게 표현할 수 있습니다.
```python
brackets = [ch for ch in sentence if ch in '(){}']
```  

<br>

## 3. 함수화 및 입력 로직 분리
검증 로직을 함수로 분리하고, `main` 함수 또는 `if __name__ == "__main__"` 블록에서 처리하면 가독성과 재사용성이 높아집니다.

<br>

# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

def is_valid_brackets(s):
    stack = []
    pairs = {')':'(', '}':'{'}
    for ch in s:
        if ch in '({':
            stack.append(ch)
        elif ch in ')}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        sentence = input().strip()
        brackets = [c for c in sentence if c in '(){}']
        result = 1 if is_valid_brackets(brackets) else 0
        print(f"#{tc} {result}")
```