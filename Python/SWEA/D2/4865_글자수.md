- [총평](#총평)
- [보완점](#보완점)
  - [1. 문자열 멤버십 검사 최적화](#1-문자열-멤버십-검사-최적화)
  - [2. `dict.get` 사용으로 예외 처리 제거](#2-dictget-사용으로-예외-처리-제거)
  - [3. 의미있는 변수명 사용](#3-의미있는-변수명-사용)
  - [4. `collections.Counter` 활용으로 코드 간소화](#4-collectionscounter-활용으로-코드-간소화)
  - [5. 공통 문자 없을 때 처리 추가](#5-공통-문자-없을-때-처리-추가)
- [최종 코드 예시](#최종-코드-예시)



<br>

# 총평
- 문제 요구사항(문자열 간 공통 문자 출현 빈도 최대값 계산)을 올바르게 구현함
- 그러나 성능 최적화 및 예외 처리, 가독성 측면에서 개선 여지가 있음
- 네이밍과 예외 처리 방식에 대한 보완 필요
- 공통 문자가 없을 때 오류 발생 가능성 존재

<br>

# 보완점
## 1. 문자열 멤버십 검사 최적화
`str1`을 `set`으로 변환해 멤버십 검사를 O(1)로 단축할 수 있습니다.
```python
char_set = set(str1)
for ch in str2:
    if ch in char_set:
        char_dict[ch] = char_dict.get(ch, 0) + 1
```
<br>

## 2. `dict.get` 사용으로 예외 처리 제거
`try/except` 대신 `dict.get` 메서드를 이용해 더 간결하게 카운팅할 수 있습니다.
```python
char_dict[ch] = char_dict.get(ch, 0) + 1
```
<br>

## 3. 의미있는 변수명 사용
`str1`, `str2`, `char2` 대신 `source`, `target`, `ch` 등으로 변경해 가독성을 높이세요.
<br>
<br>
<br>

## 4. `collections.Counter` 활용으로 코드 간소화
```python
from collections import Counter
counter = Counter(ch for ch in target if ch in set(source))
max_count = max(counter.values()) if counter else 0
```
<br>

## 5. 공통 문자 없을 때 처리 추가
`counter`(또는 `char_dict`)가 비어 있으면 `max()` 호출 시 오류가 발생하므로, 기본값(예: 0)을 설정하세요.
```python
max_count = max(counter.values()) if counter else 0
```

<br>

# 최종 코드 예시
```python
from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    source = input().strip()
    target = input().strip()
    # 공통 문자만 카운팅
    counter = Counter(ch for ch in target if ch in set(source))
    # 빈도 최대값 (없으면 0)
    max_count = max(counter.values()) if counter else 0
    print(f"#{test_case} {max_count}")
```