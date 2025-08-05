- [총평](#총평)
- [보완점](#보완점)
  - [1. 입력 처리 및 변수명 개선](#1-입력-처리-및-변수명-개선)
  - [2. 불필요한 `pass` 제거 및 조건문 단순화](#2-불필요한-pass-제거-및-조건문-단순화)
  - [3. 코드 구조화 및 함수 분리](#3-코드-구조화-및-함수-분리)
- [최종 코드 예시](#최종-코드-예시)


<br>

# 총평
- 10x10 격자를 2차원 리스트로 초기화하여 색칠 영역을 효율적으로 관리함
- 색상 정보를 1(빨강)과 2(파랑) 더하기를 통해 보라(3)를 판별하는 논리가 직관적임
- 중복 색칠 시 불필요한 덧셈을 방지하여 정확한 보라 영역 카운팅 보장

<br><br>

# 보완점
## 1. 입력 처리 및 변수명 개선
- `for _ in range(int(input())):`와 같이 직접 `input()`을 호출하기보다는, 반복 횟수를 별도 변수(`painting_count`)에 저장해 의도를 명시적으로 드러내세요.
```python
painting_count = int(input().strip())
for _ in range(painting_count):
    ...
```

<br><br>

## 2. 불필요한 `pass` 제거 및 조건문 단순화
- `if coloring_area[i][j] == color: pass`는 불필요하므로, 조건을 반대로 합쳐 `if ... != color:`로 간결하게 표현할 수 있습니다.
```python
if board[i][j] != color:
    board[i][j] += color
    if board[i][j] == 3:
        purple_count += 1
```

<br><br>

## 3. 코드 구조화 및 함수 분리
- 핵심 로직을 `solve()` 함수로 분리하고, `if __name__ == "__main__":` 블록에서 호출하면 재사용성과 테스트 가능성이 향상됩니다.
- `board`나 `grid`와 같은 더 의미 있는 변수명을 사용해 가독성을 높이세요.

<br><br>

# 최종 코드 예시
```python
import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        # 10x10 격자 초기화
        board = [[0] * 10 for _ in range(10)]
        purple_count = 0

        painting_count = int(input().strip())
        for _ in range(painting_count):
            r1, c1, r2, c2, color = map(int, input().split())
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if board[i][j] != color:
                        board[i][j] += color
                        if board[i][j] == 3:
                            purple_count += 1

        print(f"#{tc} {purple_count}")

if __name__ == "__main__":
    solve()
```  