# 기존 코드
~~~python
# 20397_돌뒤집기게임2. 돌 뒤집기 게임 2

import sys

sys.stdin = open('sample_in.txt')


def switch_stones(arr, mid, scope):
    """
    arr에서, mid를 중심으로 scope만큼 벌어져있는 각각의 원소들이
    서로 같다면 뒤집고, 다른 색이면 유지하여 다시 arr를 반환하는 함수
    Args:
        arr (list): 0과 1로 이루어진 리스트
        mid (int): 중심이 될 원소의 인덱스
        scope (int): mid에서 얼마나 떨어져있는가
    Returns:
        list: 일부 뒤집거나 유지된 arr
    """
    len_arr = len(arr)  # arr의 길이

    # 만약 범위를 벗어난다면 scope를 조정한다
    if mid - scope < 0:
        scope = mid
    if mid + scope >= len_arr:
        scope = len_arr - mid - 1  # mid + scope < len_arr 가 mid + scope <= len_arr - 1 이 되므로

    for idx in range(1, scope + 1):
        before = arr[mid - idx]
        after = arr[mid + idx]
        # 서로 같다면
        # if arr[mid - idx] == arr[mid + idx]:
        if before == after:
            # 둘 다 뒤집어준다
            arr[mid - idx] = arr[mid + idx] = (after + 1) % 2

    return arr


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 돌의 수 N, 뒤집기 횟수 M
    stones = list(map(int, input().split()))  # N 개의 돌의 상태


    for _ in range(M):  # M번에 걸쳐
        i, j = map(int, input().split())  # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해~
        result = switch_stones(stones, i - 1, j)        # i번쨰이므로 인덱스는 -1

    print(f'#{tc}', *result)
~~~
<br><br>


# 총평
- 대칭 범위 내에서 같은 색만 동시에 뒤집는 로직은 문제 의도에 맞게 잘 구현됨.
- 범위 초과 시 `scope`를 줄이는 방어 코드가 있어 런타임 에러를 예방함.
- 다만 함수가 리스트를 **제자리(in-place)**로 수정함에도 `return`값을 받아서 사용하는 혼합 설계로 인해 **`M=0`일 때 `result` 미정의** 문제가 생김.
- 범위 조정은 두 번의 `if`로 순차 보정하고 있는데, **`min(...)` 한 줄로 더 안전하고 간결하게** 표현 가능.
- 온라인 저지 환경을 고려하면 `sys.stdin = open(...)`는 제거(또는 주석)하는 편이 좋음.
<br><br>


# 보완점
## 1. 범위 계산 간소화 및 안전성 강화
- 현재는
  ```python
  if mid - scope < 0: scope = mid
  if mid + scope >= len_arr: scope = len_arr - mid - 1
  ```
  처럼 단계적으로 줄이고 있습니다. 양쪽 경계를 동시에 고려해 **최대 가능한 대칭 거리**는 `min(scope, mid, n - mid - 1)` 입니다.

~~~python
def switch_stones(arr, mid, scope):
    n = len(arr)
    scope = min(scope, mid, n - mid - 1)

    for d in range(1, scope + 1):
        if arr[mid - d] == arr[mid + d]:
            v = 1 - arr[mid - d]          # 두 값이 같으므로 한쪽 기준으로 뒤집기
            arr[mid - d] = v
            arr[mid + d] = v
    return arr
~~~


<br><br>


## 2. in-place 설계 일관화
- 함수가 리스트를 제자리 수정하므로 굳이 반환값을 사용하지 않아도 됩니다.
  - 반환값을 쓰더라도 **출력에서 `result` 대신 `stones`를 사용**해야 `M=0`에서도 안전합니다.

~~~python
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        switch_stones(stones, i - 1, j)   # 반환값 무시, in-place 수정
    print(f'#{tc}', *stones)              # 항상 안전
~~~


<br><br>


## 3. 미세 개선: 불필요한 임시 변수 축소
- `before/after` 임시 변수 없이 바로 비교해도 충분히 읽기 쉽습니다. 
  
- 다만 디버깅 중이면 유지해도 무방합니다.

~~~python
for d in range(1, scope + 1):
    if arr[mid - d] == arr[mid + d]:
        v = 1 - arr[mid - d]
        arr[mid - d] = v
        arr[mid + d] = v
~~~


<br><br>


# 최종 코드 예시
~~~python
# 20397_돌뒤집기게임2. 돌 뒤집기 게임 2

from typing import List

def switch_stones(arr: List[int], mid: int, scope: int) -> None:
    """
    중심 인덱스 mid를 기준으로 양쪽으로 scope만큼 떨어진 쌍들을 확인하여,
    같은 색(값)이면 두 돌을 동시에 뒤집는다. (서로 다르면 그대로 유지)
    리스트는 제자리(in-place)로 수정한다.
    """
    n = len(arr)
    # mid의 양옆에서 나갈 수 없는 최대 대칭 거리로 보정
    scope = min(scope, mid, n - mid - 1)

    # 대칭 쌍들을 검사하며 같은 색이면 둘 다 뒤집기
    for d in range(1, scope + 1):
        if arr[mid - d] == arr[mid + d]:
            v = 1 - arr[mid - d]   # 두 값이 같으므로 한쪽 기준으로 뒤집으면 동일
            arr[mid - d] = v
            arr[mid + d] = v


def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        stones = list(map(int, input().split()))
        for _ in range(M):
            i, j = map(int, input().split())  # 1-based i
            switch_stones(stones, i - 1, j)   # in-place 수정
        print(f'#{tc}', *stones)

if __name__ == "__main__":
    main()
~~~
