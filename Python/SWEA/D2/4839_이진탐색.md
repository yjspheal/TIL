- [총평](#총평)
- [보완점](#보완점)
  - [1. 경계 업데이트 오류 수정](#1-경계-업데이트-오류-수정)
  - [2. 함수 역할 통합 및 반환값 일관화](#2-함수-역할-통합-및-반환값-일관화)
  - [3. 중복 제거 및 가독성 향상](#3-중복-제거-및-가독성-향상)
- [최종 코드 예시](#최종-코드-예시)

<br>


# 총평
- 이진 탐색 시뮬레이션을 통해 각 참가자의 탐색 횟수를 올바르게 비교하고 승패를 판별함
- `binary_search`와 `count_search` 함수로 로직을 분리하여 재사용성과 가독성 확보
- 전체 흐름이 명확하고, 여러 테스트 케이스를 처리하기에 적합한 구조

<br><br>

# 보완점
## 1. 경계 업데이트 오류 수정
- 원래 코드에서는 `l = mid` 또는 `r = mid`로 갱신하여, 이웃한 값에 대한 탐색 시 무한 루프가 발생할 수 있습니다.
- 표준 이진 탐색처럼 `mid+1` 또는 `mid-1`을 사용해 경계를 좁히세요.
```python
# 잘못된 갱신 예시
# if target > c:
#     l = c
# else:
#     r = c

# 수정된 갱신
if target > mid:
    l = mid + 1
else:
    r = mid - 1
```
<br>

## 2. 함수 역할 통합 및 반환값 일관화
- `binary_search` 함수에서 튜플 혹은 문자열 `'end'`를 반환하는 대신, 탐색 횟수를 직접 계산하여 반환하도록 역할을 단순화하세요.
- `count_search`를 두 함수로 분리할 필요 없이, 한 함수에서 `while` 루프를 돌며 카운트를 셀 수 있습니다.
<br><br>

## 3. 중복 제거 및 가독성 향상
- `int((l + r) / 2)` 대신 `(l + r) // 2`를 사용해 명확하게 정수 나눗셈을 표현하세요.
- `input().strip()`과 `if __name__ == "__main__"` 구조를 도입해 스크립트 형태를 개선합니다.

<br><br>

# 최종 코드 예시
```python
import sys
input = sys.stdin.readline


def count_search(pages: int, target: int) -> int:
    l, r = 1, pages
    count = 0
    while True:
        mid = (l + r) // 2
        count += 1
        if mid == target:
            return count
        elif mid < target:
            l = mid + 1
        else:
            r = mid - 1


def main():
    T = int(input().strip())
    for tc in range(1, T + 1):
        pages, a, b = map(int, input().split())
        ca = count_search(pages, a)
        cb = count_search(pages, b)
        if ca < cb:
            winner = 'A'
        elif ca > cb:
            winner = 'B'
        else:
            winner = 0
        print(f"#{tc} {winner}")


if __name__ == "__main__":
    main()
```