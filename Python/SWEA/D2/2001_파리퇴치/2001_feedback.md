- [총평](#총평)
- [보완점](#보완점)
  - [1. `catch_flies` 함수에서 global 변수 사용 자제](#1-catch_flies-함수에서-global-변수-사용-자제)
  - [2. 초기값 설정 위치를 루프 밖으로 분리](#2-초기값-설정-위치를-루프-밖으로-분리)
  - [3. 내장 함수 사용 조건 여부 확인](#3-내장-함수-사용-조건-여부-확인)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문제의 요구사항을 정확하게 구현한 코드로, 정사각형 범위 내 파리 수를 합산하는 로직이 깔끔하게 잘 구성됨
- `catch_flies` 함수로 파리 수 계산을 분리한 점도 구조적으로 바람직함
- 반복문 범위도 정확히 `N - M + 1`로 설정하여 인덱스 오류 없이 안정적으로 동작함

<br><br>


# 보완점
## 1. `catch_flies` 함수에서 global 변수 사용 자제
- `M`이 함수 내부에서 전역변수로 사용되고 있으나, 명시적 인자가 아닌 글로벌 의존은 지양하는 것이 좋음
- `M`을 함수 인자로 넘기는 방식이 더 깔끔하고 유지보수에 유리함

```python
def catch_flies(arr, r, c, M):
    ...
```

그리고 호출 시:

```python
flies_count = catch_flies(fly_arr, row, col, M)
```

<br><br>


## 2. 초기값 설정 위치를 루프 밖으로 분리
- 현재 구현도 문제는 없지만, `max_flies_count = 0`을 루프 외부에 선언함으로써 테스트케이스 간 의존성에 대비한 명확성 확보

<br><br>


## 3. 내장 함수 사용 조건 여부 확인
- 문제 조건에 따라 `max()` 등을 활용한 방식으로 간결하게 구현 가능하나, 내장함수 제한이 있다면 현재 방식 유지가 적절함

<br><br>


# 최종 코드 예시
```python
def catch_flies(arr, r, c, M):
    count = 0
    for i in range(r, r + M):
        for j in range(c, c + M):
            count += arr[i][j]
    return count

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    max_flies_count = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            flies = catch_flies(fly_arr, row, col, M)
            if flies > max_flies_count:
                max_flies_count = flies

    print(f'#{tc} {max_flies_count}')
```
