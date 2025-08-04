- [총평](#총평)
- [보완점](#보완점)
  - [1. 초기값 및 매직 넘버 제거](#1-초기값-및-매직-넘버-제거)
  - [2. 슬라이딩 윈도우 적용](#2-슬라이딩-윈도우-적용)
  - [3. 변수명 간결화](#3-변수명-간결화)
- [최종 코드 예시](#최종-코드-예시)

<br>

# 총평
- 주어진 문제(구간합) 로직을 올바르게 구현했습니다.  
- 리스트 슬라이싱과 내장 함수 `sum`을 활용해 가독성이 좋습니다.

<br>

# 보완점
## 1. 초기값 및 매직 넘버 제거
- `min_sum = 100 * 100 * 10000` 같은 하드코딩 대신, 첫 번째 윈도우 합으로 초기화하여 오류 가능성을 줄이세요.

<br>

## 2. 슬라이딩 윈도우 적용
- 매 반복마다 `sum()`을 호출하면 O(N·M)의 시간 복잡도를 가지므로, 앞 숫자를 빼고 새 숫자를 더하는 슬라이딩 윈도우를 적용해 O(N)으로 개선할 수 있습니다.

<br>

## 3. 변수명 간결화
- `digit_list` → `nums` 또는 `arr`, `test_case` → `tc` 등 짧고 명확한 이름을 사용하여 가독성을 높이세요.

<br>

# 최종 코드 예시
```python
T = int(input())
for tc in range(1, T + 1):
    _, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    # 첫 윈도우 합으로 초기화
    window_sum = sum(nums[:m])
    min_sum = max_sum = window_sum

    # 슬라이딩 윈도우로 구간합 업데이트
    for i in range(m, len(nums)):
        window_sum += nums[i] - nums[i - m]
        if window_sum > max_sum:
            max_sum = window_sum
        if window_sum < min_sum:
            min_sum = window_sum

    print(f'#{tc} {max_sum - min_sum}')
