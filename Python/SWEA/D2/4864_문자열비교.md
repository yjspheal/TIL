- [총평](#총평)
- [보완점](#보완점)
  - [1. 파이썬 내장 서브스트링 검색 활용](#1-파이썬-내장-서브스트링-검색-활용)
  - [2. 불필요한 변수 및 루프 조건 단순화](#2-불필요한-변수-및-루프-조건-단순화)
  - [3. 예외 상황 처리 추가](#3-예외-상황-처리-추가)
  - [4. 입력값 `strip()` 처리로 안정성 강화](#4-입력값-strip-처리로-안정성-강화)
- [최종 코드 예시](#최종-코드-예시)


<br>

# 총평
- 주어진 `target`(패턴)이 `base`(텍스트)에 포함되는지 정확히 판별함
- 슬라이딩 윈도우 방식으로 직접 구현하여 동작 원리를 명확히 드러냄
- 입력 처리 및 결과 출력이 간결하게 작성됨

<br>

# 보완점
## 1. 파이썬 내장 서브스트링 검색 활용
현재 직접 루프와 슬라이싱을 사용해 부분 문자열을 비교하고 있으나,
파이썬의 `in` 또는 `str.find()` 메서드를 사용하면 코드가 훨씬 간결해지고
C 레벨에서 최적화된 알고리즘을 활용할 수 있습니다.
```python
# 간단히 포함 여부만 확인
isin_base = 1 if target in base else 0
```
<br>

## 2. 불필요한 변수 및 루프 조건 단순화
- `len_target`, `len_base`를 사전에 계산하는 것은 좋으나,
  직접 슬라이싱을 제거하면 변수 사용을 줄일 수 있습니다.
- 루프 대신 `for`문과 `break`를 활용하면 인덱스 관리가 더 직관적입니다.
```python
for idx in range(len(base) - len(target) + 1):
    if base[idx:idx + len(target)] == target:
        isin_base = 1
        break
```
<br>

## 3. 예외 상황 처리 추가
- `target` 길이가 `base`보다 길 경우 바로 0을 반환하도록 처리하면
  불필요한 반복을 방지할 수 있습니다.
```python
if len(target) > len(base):
    isin_base = 0
else:
    ...
```
<br>

## 4. 입력값 `strip()` 처리로 안정성 강화
입력 시 `.strip()`을 적용하면 의도치 않은 공백이나 개행 문자가 포함되는
상황을 예방할 수 있습니다.
```python
target = input().strip()
base   = input().strip()
```

<br>

# 최종 코드 예시
```python
T = int(input())
for test_case in range(1, T + 1):
    target = input().strip()
    base   = input().strip()

    # 길이 비교로 빠른 예외 처리
    if len(target) > len(base):
        isin_base = 0
    else:
        # 내장 메서드로 간결하게 체크
        isin_base = 1 if target in base else 0

    print(f"#{test_case} {isin_base}")
```  