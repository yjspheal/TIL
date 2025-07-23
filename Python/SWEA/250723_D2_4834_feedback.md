- [총평](#총평)
- [보완점](#보완점)
  - [1. 역순 처리 대신 커스텀 key를 사용한 max 함수 활용](#1-역순-처리-대신-커스텀-key를-사용한-max-함수-활용)
  - [2. 변수명 및 반복문 간소화](#2-변수명-및-반복문-간소화)
- [최종 코드 예시](#최종-코드-예시)

<br>

# 총평
- 문제 요구사항을 정확히 이해하고, 카드 개수를 세어 최댓값과 대응되는 숫자를 찾는 로직이 올바르게 구현되었습니다.  
- 입력된 문자열을 뒤집어 처리한 뒤 인덱싱으로 원래 값을 도출하는 방식으로, 카드 번호가 동일할 때 큰 숫자를 우선 처리한 점이 논리적으로 타당합니다.

<br>

# 보완점
## 1. 역순 처리 대신 커스텀 key를 사용한 max 함수 활용
파이썬의 `max` 함수에 `key=lambda x: (card_count[x], x)`를 적용하면, 카드 수와 카드 숫자를 동시에 고려해 한 번에 최댓값과 최댓값의 인덱스를 구할 수 있어 가독성이 향상됩니다.

<br>

## 2. 변수명 및 반복문 간소화
- `card_strs` 대신 `cards`와 같이 간결하면서도 의미가 분명한 변수명을 사용하고,  
- `for card_str in card_strs:` 대신 `for card in input():` 형태로 중간 변수를 줄이면 코드가 더 깔끔해집니다.

<br>

# 최종 코드 예시
```python
T = int(input())
for test_case in range(1, T + 1):
    input()  # N 값은 사용하지 않으므로 읽기만 함
    card_count = [0] * 10
    for card in input():
        card_count[int(card)] += 1
    max_card_num = max(range(10), key=lambda x: (card_count[x], x))
    print(f'#{test_case} {max_card_num} {card_count[max_card_num]}')
