- [총평](#총평)
- [보완점](#보완점)
  - [1. 부동소수점 비교의 불안정성](#1-부동소수점-비교의-불안정성)
  - [2. float 대신 fractions.Fraction 활용 (정확한 표현)](#2-float-대신-fractionsfraction-활용-정확한-표현)
  - [3. 코드 가독성·네이밍](#3-코드-가독성네이밍)
- [최종 코드 예시](#최종-코드-예시)



# 총평
전반적으로 이진수 변환 로직이 깔끔하게 구현되어 있고,
12자리까지 검사한 뒤 남은 값이 있으면 overflow 처리를 하는 아이디어도 맞습니다.
다만 몇 가지 스타일·안정성 측면에서 개선을 추천드립니다.

# 보완점
## 1. 부동소수점 비교의 불안정성
```python
elif N == 0:
    break
```

- 많은 10진 소수(예: 0.1)는 이진 부동소수로 정확히 표현되지 않아, N이 정확히 0.0이 되는 경우가 드뭅니다.
- 대신 아주 작은 값(예: 1e-12 이하)이면 0으로 간주하도록 허용하는 방식을 권장합니다.

```python
EPS = 1e-12
for exponent in range(-1, -13, -1):
    ...
    if N < EPS:
        N = 0
        break
```

==================================================================================
## 2. float 대신 fractions.Fraction 활용 (정확한 표현)
- fractions.Fraction 으로 입력값을 분수로 변환하면, 이진수 변환 시 부동소수 오차 없이 깔끔하게 처리할 수 있습니다.

```python
from fractions import Fraction

N = Fraction(input().strip())
bi_num = ''
for exponent in range(1, 13):
    N *= 2
    if N >= 1:
        bi_num += '1'
        N -= 1
    else:
        bi_num += '0'
    if N == 0:
        break
if N != 0:
    bi_num = 'overflow'

```
- 위 방식은 2**(-k) 대신, 매 반복마다 2를 곱해서 정수부만 분리하는 고전적 알고리즘으로
가독성도 좋고 오차 걱정이 없습니다.

==================================================================================

## 3. 코드 가독성·네이밍
- 변수명 bi_num 대신 binary_frac 등 좀 더 의도를 드러내는 이름을 사용하면 좋습니다.
- 주석으로 “왜 이렇게 하는지”를 한 줄 더 달아 놓으면, 나중에 읽을 때 이해가 빠릅니다.



# 최종 코드 예시
```python
from fractions import Fraction

T = int(input())
for tc in range(1, T + 1):
    # Fraction을 이용해 정확한 분수 표현
    N = Fraction(input().strip())
    binary_frac = ''
    
    for _ in range(12):            # 최대 12자리 시도
        N *= 2
        if N >= 1:
            binary_frac += '1'
            N -= 1
        else:
            binary_frac += '0'
        if N == 0:                # 0이 되면 더 이상 연산 불필요
            break

    if N != 0:
        result = 'overflow'
    else:
        result = binary_frac

    print(f'#{tc} {result}')
```

*장점*
- Fraction 으로 부동소수 오차 제거
- 반복마다 2를 곱해 처리하니 2**exponent 계산 불필요
- 깔끔한 변수명과 구조
