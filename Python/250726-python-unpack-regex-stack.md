- [\[학습 1\] unpack \*, \*\*에 대하여](#학습-1-unpack--에-대하여)
  - [내용](#내용)
  - [예시](#예시)
  - [추가 학습](#추가-학습)
- [\[학습 2\] 정규표현식 정리](#학습-2-정규표현식-정리)
  - [내용](#내용-1)
  - [주요 메서드](#주요-메서드)
  - [추가 학습](#추가-학습-1)
- [\[학습 3\] Python에서의 Stack에 관하여](#학습-3-python에서의-stack에-관하여)
  - [내용](#내용-2)
  - [주요 연산](#주요-연산)
  - [추가 학습](#추가-학습-2)

---

# [학습 1] unpack *, **에 대하여

## 내용

- Python에서 `*`와 `**`는 주로 함수의 매개변수에서 사용
- 다양한 형태로 데이터를 언패킹(unpacking)하거나 **매개변수**를 처리하는 데 유용

## 예시

- **`*`**: **튜플**이나 **리스트**에서 값을 **언패킹**할 때 사용됨
  
```python
# 예시 1: 리스트 언패킹
a, *b = [1, 2, 3, 4]
print(a)  # 1
print(b)  # [2, 3, 4]
```

- **`**`**: **딕셔너리**에서 **키-값** 쌍을 **언패킹**하거나, 함수의 키워드 매개변수를 처리할 때 사용됨
  
```python
# 예시 2: 딕셔너리 언패킹
def func(**kwargs):
    print(kwargs)

func(name="Alice", age=25)  # {'name': 'Alice', 'age': 25}
```

## 추가 학습

- `*args`와 `**kwargs`를 통해 **가변 인수**를 처리
<br><br>


# [학습 2] 정규표현식 정리

## 내용

- 정규표현식(Regular Expression, `re`)은 문자열에서 특정 패턴을 검색하고, 이를 처리하는 강력한 도구
- Python에서는 `re` 모듈을 사용하여 정규표현식을 다룰 수 있음

```python
import re

# 예시 1: 정규표현식으로 패턴 찾기
pattern = r'\d+'  # 숫자 1개 이상
text = "My phone number is 12345."
matches = re.findall(pattern, text)
print(matches)  # ['12345']
```

## 주요 메서드

- **`re.match()`**: 문자열의 시작에서부터 패턴을 찾음
- **`re.search()`**: 문자열 전체에서 패턴을 찾음
- **`re.findall()`**: 패턴에 맞는 모든 부분을 list로 반환
- **`re.sub()`**: 문자열 내에서 패턴을 찾아 교체

## 추가 학습

- **문자 클래스**: `[abc]`, `\d`, `\w`, `\s` 등.
- **수량자**: `*`, `+`, `?`, `{n,m}` 등.
- **그룹핑**: `()`, `(?:)` 등을 활용하여 캡처 그룹 생성

<br><br>


# [학습 3] Python에서의 Stack에 관하여

## 내용

- **Stack**은 **후입선출(LIFO)** 방식으로 작동하는 자료구조
- Python에서는 **리스트**를 사용하여 스택을 구현할 수 있음

```python
# 스택 구현 예시
stack = []
stack.append(1)  # 스택에 값 추가
stack.append(2)
print(stack)  # [1, 2]
stack.pop()    # 스택에서 값 제거
print(stack)  # [1]
```

## 주요 연산

- **`append()`**: 스택의 **top**에 값을 추가
- **`pop()`**: 스택의 **top**에서 값을 제거하고 반환
- **`peek()`**: 스택의 **top** 값을 확인 (단, Python의 리스트는 `peek()` 메서드를 지원하지 않으므로 직접 구현해야 합니다.)

```python
# peek() 함수 구현 예시
def peek(stack):
    if stack:
        return stack[-1]
    return None

print(peek(stack))  # 1
```


## 추가 학습

- **Deque**: Python에서는 `collections.deque`를 사용하여 더 효율적인 스택과 큐를 구현할 수 있음
  
```python
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.pop()  # 2
```
