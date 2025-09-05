- [1. defaultdict란?](#1-defaultdict란)
- [2. 사용법 및 예시](#2-사용법-및-예시)
- [3. 기본값 팩토리(Default Factory) 종류](#3-기본값-팩토리default-factory-종류)
- [4. 일반 딕셔너리와의 비교](#4-일반-딕셔너리와의-비교)
  - [일반 dict 사용 시](#일반-dict-사용-시)
  - [defaultdict 사용 시](#defaultdict-사용-시)

---

## 1. defaultdict란?

- 파이썬의 `collections` 모듈에 포함된 딕셔너리(dict)의 서브클래스
- 딕셔너리에서 존재하지 않는 키(key)에 접근할 때 발생하는 `KeyError`를 방지하는 기능
- 키가 없을 경우, 에러를 발생시키는 대신 생성 시 지정된 `기본값 팩토리(default_factory)` 함수를 호출하여 기본값을 생성하고 반환함

## 2. 사용법 및 예시

- `defaultdict`를 생성할 때 `default_factory`를 인자로 전달
- 이 팩토리 함수는 키가 없을 때 호출되어 기본값을 동적으로 생성

```python
from collections import defaultdict

# int를 팩토리로 지정 -> 기본값으로 0이 생성됨
word_counts = defaultdict(int)

for word in ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']:
    word_counts[word] += 1 # 키가 없어도 KeyError 없이 0을 기본값으로 하여 1이 더해짐

# word_counts -> defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})


# list를 팩토리로 지정 -> 기본값으로 빈 리스트 []가 생성됨
graph = defaultdict(list)
graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('C')

# graph -> defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['C']})
```

## 3. 기본값 팩토리(Default Factory) 종류

- `default_factory`는 인자 없이 호출 가능해야 하며, 기본값을 반환해야 함
- 자주 사용되는 팩토리:
    - `int`: 기본값 `0`
    - `float`: 기본값 `0.0`
    - `str`: 기본값 `''` (빈 문자열)
    - `list`: 기본값 `[]` (빈 리스트)
    - `set`: 기본값 `set()` (빈 집합)
- `lambda`를 사용하여 커스텀 기본값을 지정할 수도 있음
    - `d = defaultdict(lambda: "N/A")`

## 4. 일반 딕셔너리와의 비교

- `defaultdict`를 사용하면 존재하지 않는 키에 대한 예외 처리를 할 필요가 없어 코드가 깔끔하고 가독성이 높아짐

### 일반 dict 사용 시
```python
d = {}
# d['a'] += 1 -> KeyError 발생

# KeyError를 피하기 위한 코드
if 'a' not in d:
    d['a'] = 0
d['a'] += 1

# 또는 setdefault() 사용
d.setdefault('a', 0)
d['a'] += 1
```

### defaultdict 사용 시
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1 # 코드가 훨씬 간결해짐
```
