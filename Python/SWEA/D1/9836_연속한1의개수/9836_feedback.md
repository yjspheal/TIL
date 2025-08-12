- [총평](#총평)
- [보완점](#보완점)
  - [1. `int` 변환 제거로 연산량 절감](#1-int-변환-제거로-연산량-절감)
  - [2. 문자열 순회 간결화](#2-문자열-순회-간결화)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문자열을 한 번만 순회하며 연속된 `1`의 개수를 세어 최대값을 갱신하는 로직이 올바르게 작성됨
- `current_ones`와 `max_ones`를 분리하여 상태 추적을 명확히 구현함
- 문제 요구사항에 맞춰 테스트 케이스마다 결과를 출력하는 구조가 적절함

<br><br>

# 보완점
## 1. `int` 변환 제거로 연산량 절감
문자 하나씩 `int(str_bin[i])`로 변환하는 대신, 직접 문자 비교(`str_bin[i] == '1'`)를 사용하면 불필요한 형 변환 비용을 줄일 수 있습니다.
```python
if str_bin[i] == '1':
    current_ones += 1
    ...
```

<br><br>
## 2. 문자열 순회 간결화
인덱스 대신 문자열 자체를 순회하면 코드가 더 간결해집니다.
```python
for ch in str_bin.strip():
    if ch == '1':
        current_ones += 1
        if current_ones > max_ones:
            max_ones = current_ones
    else:
        current_ones = 0
```

<br><br>
# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    s = input().strip()

    max_ones = 0
    current_ones = 0
    for ch in s:
        if ch == '1':
            current_ones += 1
            if current_ones > max_ones:
                max_ones = current_ones
        else:
            current_ones = 0

    print(f"#{tc} {max_ones}")
```