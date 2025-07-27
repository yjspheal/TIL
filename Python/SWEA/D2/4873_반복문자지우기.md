
- [총평](#총평)
- [보완점](#보완점)
  - [1. 반환 타입 일관성 및 문서화](#1-반환-타입-일관성-및-문서화)
  - [2. 타입 힌트 추가로 가독성 강화](#2-타입-힌트-추가로-가독성-강화)
  - [3. `pop` 시 언더바 변수 생략](#3-pop-시-언더바-변수-생략)
  - [4. 불필요한 import 제거 또는 자료구조 검토](#4-불필요한-import-제거-또는-자료구조-검토)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- LIFO 스택 구조를 활용해 반복 문자를 제거하는 로직을 올바르게 구현함
- 문자열을 한 번만 순회하여 O(n) 시간에 처리하는 효율적인 알고리즘
- 함수 분리로 가독성과 재사용성 확보

<br>

# 보완점
## 1. 반환 타입 일관성 및 문서화
- 현재 `remove_same_char`는 리스트를 반환하지만, 호출부에서는 길이만 사용합니다.
- 나중에 문자열 결과가 필요할 경우, 문자열로 반환하거나 반환 타입을 명확히 문서화하면 좋습니다.
```python
# 문자열로 반환할 수도 있음
return ''.join(char_stack)
```

<br>
## 2. 타입 힌트 추가로 가독성 강화
- 함수에 타입 힌트를 추가하면 IDE 지원 및 타입 검사 도구 활용에 도움이 됩니다.
```python
from typing import List

def remove_same_char(chars: str) -> List[str]:
    ...
```

<br>
## 3. `pop` 시 언더바 변수 생략
- `_ = char_stack.pop()` 대신 `char_stack.pop()`만 호출해도 충분합니다.
```python
else:
    char_stack.pop()
```

<br>
## 4. 불필요한 import 제거 또는 자료구조 검토
- 현재 로직에서는 리스트만으로 충분하므로 `deque` 등 다른 자료구조는 불필요합니다.
- 향후 양쪽 끝 연산이 필요하다면 `collections.deque`를 고려하세요.

<br>
# 최종 코드 예시
```python
from typing import List

def remove_same_char(chars: str) -> List[str]:
    char_stack: List[str] = []
    for char in chars:
        if not char_stack or char_stack[-1] != char:
            char_stack.append(char)
        else:
            char_stack.pop()
    return char_stack  # 필요 시 ''.join(char_stack)로 문자열 반환

if __name__ == "__main__":
    T = int(input().strip())
    for tc in range(1, T+1):
        sentence = input().strip()
        result = remove_same_char(sentence)
        print(f"#{tc} {len(result)}")
```  