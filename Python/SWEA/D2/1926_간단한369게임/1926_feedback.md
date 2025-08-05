- [총평](#총평)
- [보완점](#보완점)
  - [1. `count_369` 계산 위치 수정](#1-count_369-계산-위치-수정)
  - [2. 변수 재사용 피하고 가독성 높이기](#2-변수-재사용-피하고-가독성-높이기)
  - [3. 각 자리별 검사로 단순화](#3-각-자리별-검사로-단순화)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 369 게임의 핵심 로직(숫자의 각 자리에서 3·6·9 개수만큼 '-' 출력)을 구현함
- 연속된 숫자에 대해 '-'를 반복 출력해 문제 요구사항을 충족함
- 입력 및 출력 흐름이 전체적으로 올바르게 구성됨

<br><br>

# 보완점
## 1. `count_369` 계산 위치 수정
현재 각 자릿수마다 `for i in range(len(n))` 안에서 `n.count()`를 반복 호출하고 있어 불필요한 반복 연산이 발생합니다. 반복문 없이 문자열을 한 번만 순회하여 카운트를 계산하도록 위치를 이동하세요.
```python
s = str(num)
count_369 = s.count('3') + s.count('6') + s.count('9')
```

<br><br>
## 2. 변수 재사용 피하고 가독성 높이기
루프 변수 `n`을 문자열로 재할당하면 타입 혼동이 생길 수 있습니다. 숫자와 문자열을 별도 변수로 분리해 명확히 구분하세요.
```python
for num in range(1, N + 1):
    s = str(num)
    ...
```

<br><br>
## 3. 각 자리별 검사로 단순화
`.count()` 대신 리스트 컴프리헨션과 `sum`을 사용하면 코드가 더 간결하고 의도가 분명해집니다.
```python
count_369 = sum(ch in '369' for ch in s)
```

<br><br>
# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

N = int(input().strip())
for num in range(1, N + 1):
    s = str(num)
    count_369 = sum(ch in '369' for ch in s)
    if count_369:
        print('-' * count_369, end=' ')
    else:
        print(num, end=' ')
```