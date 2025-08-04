- [총평](#총평)
- [보완점](#보완점)
  - [1. 전역 변수(`min_sum`) 제거 및 클로저 사용](#1-전역-변수min_sum-제거-및-클로저-사용)
  - [2. 비트마스크로 `visited` 리스트 대체](#2-비트마스크로-visited-리스트-대체)
  - [3. 문제 규모가 크다면 헝가리안 알고리즘 검토](#3-문제-규모가-크다면-헝가리안-알고리즘-검토)
- [최종 코드 예시](#최종-코드-예시)


<br><br>
# 총평
- DFS(백트래킹)를 통해 각 행마다 가능한 열을 재귀로 탐색하며 최소 합을 정확히 계산함
- 현재 합이 `min_sum`을 넘으면 조기 종료하는 가지치기(pruning)를 적용해 성능을 개선함
- `visited` 리스트를 사용해 선택된 열을 관리하여 중복 선택을 방지함

<br><br>
# 보완점
## 1. 전역 변수(`min_sum`) 제거 및 클로저 사용
- 전역 변수 대신 함수 내부 클로저를 활용해 상태를 관리하면 코드의 가독성과 안전성이 높아집니다.
```python
def solve_case(arr):
    N = len(arr)
    answer = float('inf')
    def dfs(row, current, used):
        nonlocal answer
        if current >= answer:
            return
        if row == N:
            answer = current
            return
        for col in range(N):
            if not (used >> col) & 1:
                dfs(row+1, current + arr[row][col], used | (1 << col))
    dfs(0, 0, 0)
    return answer
```

<br><br>
## 2. 비트마스크로 `visited` 리스트 대체
- `visited` 리스트 대신 정수 비트마스크로 열 선택 상태를 표현하면 메모리와 검사 비용을 줄일 수 있습니다.
```python
# used: 0 비트는 선택되지 않음, 1 비트는 이미 선택됨
if not (used >> col) & 1:
    dfs(..., used | (1 << col))
```


<br><br>
## 3. 문제 규모가 크다면 헝가리안 알고리즘 검토
- 행렬 크기 \(N\)이 100 이상으로 커지면 이 방식은 비효율적입니다.
- 이 경우 이중 할당 문제(assignment problem)를 헝가리안 알고리즘으로 \(O(N^3)\)에 해결할 수 있습니다.

<br><br>
# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

def solve_case(arr):
    N = len(arr)
    answer = float('inf')
    def dfs(row, current, used):
        nonlocal answer
        if current >= answer:
            return
        if row == N:
            answer = current
            return
        for col in range(N):
            if not (used >> col) & 1:
                dfs(row+1, current + arr[row][col], used | (1 << col))
    dfs(0, 0, 0)
    return answer

if __name__ == '__main__':
    T = int(input().strip())
    for tc in range(1, T+1):
        N = int(input().strip())
        arr = [list(map(int, input().split())) for _ in range(N)]
        result = solve_case(arr)
        print(f"#{tc} {result}")
```  