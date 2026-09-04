- [Python .sort() 심화 활용법](#python-sort-심화-활용법)
  - [1. `key` 매개변수](#1-key-매개변수)
  - [2. `lambda` 함수 활용](#2-lambda-함수-활용)
  - [3. 사용자 정의 함수 활용](#3-사용자-정의-함수-활용)
  - [4. 딕셔너리 정렬](#4-딕셔너리-정렬)
  - [5. 다중 조건 정렬](#5-다중-조건-정렬)

---
<br>
<br>

# Python .sort() 심화 활용법

## 1. `key` 매개변수
- 리스트의 `sort()` 메서드는 `key` 매개변수를 통해 정렬 기준을 지정할 수 있음
- `key`에는 각 요소에 대해 호출될 함수를 전달하며, 이 함수의 반환값이 정렬의 기준이 됨

## 2. `lambda` 함수 활용
- 간단한 정렬 기준은 `lambda` 함수를 사용하여 한 줄로 정의 가능
- 예시: 튜플의 두 번째 요소를 기준으로 리스트 정렬
```python
data = [(1, 5), (3, 2), (2, 8)]
data.sort(key=lambda x: x[1])
# data: [(3, 2), (1, 5), (2, 8)]
```

## 3. 사용자 정의 함수 활용
- 복잡한 정렬 로직이 필요할 경우, 별도의 함수를 정의하여 `key`에 전달 가능
- 예시: 문자열의 길이를 기준으로 정렬
```python
def get_length(s):
    return len(s)

words = ['apple', 'banana', 'cherry', 'kiwi']
words.sort(key=get_length)
# words: ['kiwi', 'apple', 'banana', 'cherry']
```
- `key=len`과 같이 내장 함수를 직접 사용할 수도 있음

## 4. 딕셔너리 정렬
- 리스트 안에 딕셔너리가 있을 경우, 특정 키의 값을 기준으로 정렬할 수 있음
```python
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
students.sort(key=lambda item: item['score'])
# score가 낮은 순으로 정렬됨
```

## 5. 다중 조건 정렬
- 튜플을 반환하는 `lambda`를 사용하여 여러 기준으로 정렬할 수 있음
- 첫 번째 기준이 같을 경우 두 번째 기준으로 정렬됨
- 예시: 점수가 높은 순, 점수가 같다면 이름 오름차순으로 정렬
```python
students = [
    {'name': 'David', 'score': 92},
    {'name': 'Bob', 'score': 92},
    {'name': 'Alice', 'score': 85}
]
students.sort(key=lambda item: (-item['score'], item['name']))
# 결과: Bob, David, Alice 순
# 점수(score)는 내림차순(- 사용), 이름(name)은 오름차순
```
- **중요**: 내림차순 정렬을 위해 숫자형 데이터에 `-`를 붙이는 트릭을 활용함
