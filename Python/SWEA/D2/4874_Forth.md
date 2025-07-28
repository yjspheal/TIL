- [총평](#총평)
- [보완점](#보완점)
  - [1. 연산자 목록 스코프 및 매핑 방식 개선](#1-연산자-목록-스코프-및-매핑-방식-개선)
  - [2. 예외 처리 구체화 및 불필요한 `try/except` 제거](#2-예외-처리-구체화-및-불필요한-tryexcept-제거)
  - [3. 반환 타입 및 흐름 통일성 확보](#3-반환-타입-및-흐름-통일성-확보)
  - [4. 코드 간결화 및 반복 제거](#4-코드-간결화-및-반복-제거)
- [최종 코드 예시](#최종-코드-예시)

<br><br>
# 총평
- 스택을 이용해 Forth 식을 한 번 순회하며 연산과 출력 로직을 처리하는 구조가 적절함
- 숫자, 연산자, 출력 기호(`.`)를 분기 처리하여 기본 요구사항을 충족함
- 에러 상황을 조기 반환(return)하도록 설계해 가독성이 비교적 좋음

<br><br>

# 보완점
## 1. 연산자 목록 스코프 및 매핑 방식 개선
현재 `operators` 리스트를 전역에 정의한 후 함수 내에서 참조하고 있습니다. 이를 함수 내부로 옮기거나, 연산자별 행동을 매핑한 딕셔너리를 사용해 명확히 분리하세요.
```python
# 함수 내에 매핑을 정의
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
```
<br><br>

## 2. 예외 처리 구체화 및 불필요한 `try/except` 제거
`except:`로 모든 예외를 잡기보다, `IndexError`만 캡처해 스택 언더플로우를 처리하세요. 또한 숫자 변환에 `element.isdecimal()` 대신 `str.isdigit()`이나 `int()` 캐스팅을 사용해 오류를 명시적으로 처리할 수 있습니다.
```python
try:
    b = stack.pop()
    a = stack.pop()
except IndexError:
    return 'error'
```
<br><br>

## 3. 반환 타입 및 흐름 통일성 확보
현재 `.` 처리 시 즉시 `return`하고, 루프가 끝나면 `'error'`를 반환합니다. 에러는 모두 문자열 `'error'`로 통일하되, 정상 결과는 정수 타입으로 반환하도록 명확히 주석으로 문서화하세요.
<br><br>

## 4. 코드 간결화 및 반복 제거
- `_ = num1 + num2` 식으로 중간 변수에 담지 말고 결과를 바로 `stack.append(...)`에 사용
- 숫자 검사와 연산자 검사를 `if-elif-else` 체계로 통합해 가독성 향상

<br><br>

# 최종 코드 예시
```python
from typing import List, Union

def calculate_forth(tokens: List[str]) -> Union[int, str]:
    """
    Forth 식을 계산하여 결과(정수) 또는 'error'를 반환합니다.
    """ 
    stack: List[int] = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }

    for tok in tokens:
        if tok.isdigit():
            stack.append(int(tok))
        elif tok in ops:
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[tok](a, b))
        elif tok == '.':
            # 출력 지시: 스택에 정확히 1개 있어야 정상
            return stack[0] if len(stack) == 1 else 'error'
        else:
            return 'error'

    # 반복문 종료 후에도 출력 지시가 없으면 에러
    return 'error'

if __name__ == '__main__':
    T = int(input().strip())
    for tc in range(1, T + 1):
        tokens = input().split()
        result = calculate_forth(tokens)
        print(f"#{tc} {result}")
```  