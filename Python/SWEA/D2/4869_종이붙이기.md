- [총평](#총평)
- [보완점](#보완점)
  - [1. 동적 계획법(DP) 활용으로 시간·공간 효율 극대화](#1-동적-계획법dp-활용으로-시간공간-효율-극대화)
  - [2. 불필요한 함수 구현 제거 및 표준 라이브러리 활용](#2-불필요한-함수-구현-제거-및-표준-라이브러리-활용)
  - [3. 코드 구조화 및 입력 처리 강화](#3-코드-구조화-및-입력-처리-강화)
- [최종 코드 예시](#최종-코드-예시)


<br>

# 총평
- 주어진 `row_length`에 대해 큰 종이(길이 2)와 작은 종이(길이 1)를 활용해 모든 배치 경우를 올바르게 산출함
- 조합식을 통해 각 `big_paper` 수에 대한 경우의 수를 계산하는 접근이 수학적으로 타당함
- 그러나 `factorial` 함수를 직접 구현해 사용함에 따라 계산 비용이 커질 수 있고, 코드 가독성 및 유지보수가 다소 떨어짐

<br>
<br>

# 보완점
## 1. 동적 계획법(DP) 활용으로 시간·공간 효율 극대화
팩토리얼과 조합 계산을 반복 호출하는 대신, 다음 점화식을 통해 O(N) 시간과 O(N) 공간으로 해결할 수 있습니다.
```python
# F[n] = F[n-1] + 2 * F[n-2]
# 베이스: F[0] = 1, F[1] = 1

def count_tilings(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n]
```
이 방식은 `factorial` 호출 없이 선형 스캔 만으로 결과를 얻어 대규모 입력에도 적합합니다.
<br>
<br>
<br>

## 2. 불필요한 함수 구현 제거 및 표준 라이브러리 활용
- 직접 작성한 `factorial` 대신 `math.comb`를 사용하면 조합 계산이 간단해집니다.
```python
from math import comb
case_count += comb(whole_paper, big_paper) * (2 ** big_paper)
```
- 그러나 DP 방식이 더 직관적이고 빠릅니다.
<br>
<br>
<br>

## 3. 코드 구조화 및 입력 처리 강화
- 검증 로직을 함수로 분리하고 `if __name__ == "__main__"` 블록에서 입력 처리
- `input().strip()` 사용으로 공백 이슈 방지

<br>
<br>
<br>

# 최종 코드 예시
```python
import sys

def count_tilings(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n]

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        # 길이 10 단위로 입력되므로 10으로 나눈 값이 n
        n = int(input().strip()) // 10
        result = count_tilings(n)
        print(f"#{tc} {result}")
```  