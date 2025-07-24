
- [\[학습1\] `filter(function, iterable)` 함수](#학습1-filterfunction-iterable-함수)
  - [내용](#내용)
  - [예시](#예시)
- [\[학습2\] `max(range(n), key=lambda x: (arr[x], x)` 의 이해](#학습2-maxrangen-keylambda-x-arrx-x-의-이해)
  - [내용](#내용-1)
  - [설명](#설명)
  - [예시](#예시-1)
- [\[학습3\] 다른 경로에 있는 패키지를 사용하는 방법](#학습3-다른-경로에-있는-패키지를-사용하는-방법)
  - [내용](#내용-2)
  - [해결 방법](#해결-방법)
- [\[학습4\] pprint란 무엇인가?](#학습4-pprint란-무엇인가)
  - [내용](#내용-3)
  - [예시](#예시-2)
  - [주의사항](#주의사항)


<br><br>

# [학습1] `filter(function, iterable)` 함수

## 내용
- 주어진 **함수**를 **iterable** 객체에 적용하여, 그 함수가 **True**를 반환하는 요소들만 걸러내는 함수
- `map`이나 `range`처럼 **지연 평가**(lazy evaluation) 방식으로 동작
  - (한 번에 계산하지 않고 필요한 시점에 데이터를 반환하는 방식)
- 반환값은 **iterator**이므로, 값을 출력하려면 `list`나 `tuple`로 변환해야 함.


<br><br>

## 예시
```python
numbers = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x % 2 == 0, numbers))  # 짝수만 필터링
print(filtered)  # [2, 4]
```

- **`filter(function, iterable)`**: 
  - `function`: 각 요소에 적용할 조건을 정의하는 함수 (예: `lambda x: x % 2 == 0`)
  - `iterable`: 필터링할 iterable 데이터 (예: 리스트)


<br><br><br><br>

# [학습2] `max(range(n), key=lambda x: (arr[x], x)` 의 이해

## 내용

- max는 기본적으로 iterable의 요소 자체를 비교하여 최대값을 반환하지만,
- key 인자 사용 시 내부적으로 **먼저** `key(요소)`를 계산하고 그 결과값끼리 비교하여 최대 결과값을 반환함

<br>

## 설명

- **`max(range(n))`**: `0`부터 `n-1`까지의 값을 아래 key에 따라 계산
- **`key=lambda x: (arr[x], x)`**: `arr[x]` 값(첫 번째 기준)을 먼저 비교하고, **값이 동일하면 인덱스**, 즉 `x`를 비교하여 최댓값을 찾습니다.

<br><br>

## 예시

```python
arr = [10, 20, 30, 15, 30]
mode = max(range(5), key=lambda x: (arr[x], x))  # 4 (index)
```

- **동점자 처리**: `arr[x]` 값이 동일하면, 더 **큰 인덱스를 우선 선택**하는 방식입니다.

<br><br><br><br>

# [학습3] 다른 경로에 있는 패키지를 사용하는 방법

## 내용

Python에서는 기본적으로 설치된 경로 외의 다른 경로에 있는 패키지를 사용하려면, `sys.path`에 해당 경로를 추가하거나, **환경 변수**를 설정하여 패키지를 불러올 수 있습니다.

<br><br>

## 해결 방법

1. `sys.path.append()`를 사용하여 경로 추가:

```python
import sys
sys.path.append('/path/to/your/package')
import your_package
```

2. `PYTHONPATH` 환경 변수를 사용하여 경로 추가:

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/your/package
```

이렇게 하면, 여러 프로젝트에서 공통으로 사용하는 패키지를 관리할 수 있습니다.

- 근데 이렇게 할 일이 있나..?
---

<br><br>

# [학습4] pprint란 무엇인가?

## 내용

- **Pretty Print**의 약자
- 데이터를 **보기 쉽게 출력**해주는 Python 모듈
- **복잡한 데이터 구조** 등을 정렬하고 **들여쓰기** 해줌
  - ex) dictionary, list



## 예시


```python
from pprint import pprint

data = {"name": "Alice", "age": 25, "address": {"city": "Wonderland", "zip": "12345"}}
pprint(data)



# 아래처럼 출력
"""
{'age': 25,
 'address': {'city': 'Wonderland', 'zip': '12345'},
 'name': 'Alice'}
 """
```

## 주의사항
- `pprint`는 최대 5개의 위치 인자를 받을 수 있음
  - 위치 인자 1: object 
  - 위치 인자 2: stream (실제로 파일 같은 객체여야 함)
  - 위치 인자 3: indent (int('c') 불가 → 에러)
  - 위치 인자 4: width 
  - 위치 인자 5: depth
- 따라서 print처럼 `pprint(a, b, c, d)` 하다가 에러날 수 있으니 주의