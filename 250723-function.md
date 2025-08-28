# TIL - 2025-07-24

- [궁금증 1 - 언패킹 시 변수 개수가 맞지 않으면?](#궁금증-1---언패킹-시-변수-개수가-맞지-않으면)
  - [해결](#해결)
- [궁금증 2 - 딕셔너리 언패킹 시, 키와 매개변수 이름이 일치해야 하나?](#궁금증-2---딕셔너리-언패킹-시-키와-매개변수-이름이-일치해야-하나)
  - [해결](#해결-1)
- [궁금증 3 - map 객체는 왜 바로 출력되지 않을까?](#궁금증-3---map-객체는-왜-바로-출력되지-않을까)
  - [해결](#해결-2)
  - [더 알아볼 점](#더-알아볼-점)

---

## 궁금증 1 - 언패킹 시 변수 개수가 맞지 않으면?

```python
a, b = [1, 2, 3]
```

### 해결

- **ValueError: too many values to unpack** 에러 발생
- 언패킹 시, **왼쪽 변수 개수 == 오른쪽 값 개수**가 일치해야 함
- 예외적으로, `*`를 이용한 가변 언패킹은 일부 허용됨

```python
a, *b = [1, 2, 3]   # a=1, b=[2, 3]
```

---

## 궁금증 2 - 딕셔너리 언패킹 시, 키와 매개변수 이름이 일치해야 하나?

```python
def greet(name):
    print(f"Hello, {name}")

person = {"name": "Alice"}
greet(**person)  # ✅ 동작
```

### 해결

- `**dict`로 언패킹할 경우, **딕셔너리의 키와 함수의 매개변수 이름이 정확히 일치해야 한다**
- 일치하지 않으면 `TypeError` 발생

```python
wrong = {"nickname": "Bob"}
greet(**wrong)  # ❌ TypeError: greet() got an unexpected keyword argument 'nickname'
```

---

## 궁금증 3 - map 객체는 왜 바로 출력되지 않을까?

```python
result = map(str, [1, 2, 3])
print(result)
```

```text
<map object at 0x...>  # 👀 원하는 결과 아님
```

### 해결

- `map`은 **지연 평가(lazy evaluation)** 방식으로 동작하는 **iterator** 객체
- 실제 데이터를 사용하려면 `list()`, `for` 루프 등을 이용해 **소비(consumption)** 해야 함

```python
list(result)  # ['1', '2', '3']
```

### 더 알아볼 점

- `iterable`과 `iterator`의 차이
- map, filter, generator 등 Python의 lazy evaluation 구조 전반
- `map`은 한 번 소비하면 다시 사용할 수 없는 일회성임 (재사용하려면 list 등으로 변환 필요)
