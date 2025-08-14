- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 else 제거 및 간결화](#1-불필요한-else-제거-및-간결화)
  - [2. 내장 연산 활용 (간단 버전)](#2-내장-연산-활용-간단-버전)
  - [3. 고급 알고리즘(KMP) 적용 예시](#3-고급-알고리즘kmp-적용-예시)
- [최종 코드 예시 (간단 + 유지보수성 강화)](#최종-코드-예시-간단--유지보수성-강화)


# 기존 코드
~~~python
# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
# import sys
# sys.stdin = open("sample_input.txt")

def brute_force(p, t):
    """
    문자열 t에서 문자열 p라는 패턴이 존재하는지 여부를 반환하는 함수
    Args:
        p (str): 찾고자 하는 패턴
        t (str): 원본 문자열
    Returns:
        int: 존재한다면 1 없다면 0을 반환
    """
    i = 0       # t의 인덱스
    j = 0       # p의 인덱스

    len_p = len(p)           # N
    len_t = len(t)           # M

    # t와 p가 일치하는지 한자리씩 확인
    while i < len_t and j < len_p:
        if t[i] == p[j]:        # 서로 같으면
            i += 1
            j += 1              # 두 인덱스에 += 1
        else:                   # 다르면
            i = i - j + 1       # 타겟 시작점은 처음 + 1로 돌아가고
            j = 0               # 패턴 시작점은 0으로 초기화

    # while을 다 돌았는데 j가 len_p라면 패턴이 존재하는 것
    if j == len_p:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    pattern = input()        # 길이 N의 문자열
    target = input()         # 길이 M의 문자열

    has_pattern = brute_force(pattern, target)
    
    print(f'#{test_case} {has_pattern}')
~~~
<br><br>


# 총평
- 전형적인 **Brute Force 문자열 매칭 알고리즘**(O(N×M))을 잘 구현했습니다.
- 인덱스 `i`와 `j`를 이용해 불일치 시 `i`를 `i-j+1`로 이동시키고 `j`를 0으로 초기화하는 방식이 표준입니다.
- 동작상 문제는 없지만, 파이썬 내장 `"substr in str"` 연산이나 `.find()`를 쓰면 훨씬 간단합니다.
- 대규모 문자열에서는 KMP, Boyer–Moore 같은 고급 알고리즘으로 최적화 가능.
- 함수가 `1`/`0`을 반환하므로 호출부에서 그대로 출력하는 구조도 깔끔합니다.
<br><br>


# 보완점
## 1. 불필요한 else 제거 및 간결화
- 마지막 `if j == len_p:`는 True/False 결과를 `int()`로 변환하면 더 간단.
~~~python
return int(j == len_p)
~~~

<br><br>


## 2. 내장 연산 활용 (간단 버전)
- 같은 동작을 파이썬 내장 연산으로 대체하면 코드가 크게 줄어듭니다.
~~~python
def contains_pattern(p: str, t: str) -> int:
    return int(p in t)
~~~

<br><br>


## 3. 고급 알고리즘(KMP) 적용 예시
- 입력 크기가 매우 클 경우 KMP를 쓰면 O(N+M)으로 처리 가능.
~~~python
def kmp_search(p: str, t: str) -> int:
    # LPS 배열 생성
    lps = [0] * len(p)
    length = 0
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # 매칭
    i = j = 0
    while i < len(t):
        if p[j] == t[i]:
            i += 1
            j += 1
        if j == len(p):
            return 1
        elif i < len(t) and p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return 0
~~~


<br><br>


# 최종 코드 예시 (간단 + 유지보수성 강화)
~~~python
# 4864. 문자열 비교

def brute_force(p: str, t: str) -> int:
    """문자열 t에서 p가 존재하면 1, 아니면 0 반환"""
    i = j = 0
    len_p, len_t = len(p), len(t)

    while i < len_t and j < len_p:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    return int(j == len_p)

def main() -> None:
    T = int(input())
    for test_case in range(1, T + 1):
        pattern = input().strip()
        target = input().strip()
        print(f'#{test_case} {brute_force(pattern, target)}')

if __name__ == "__main__":
    main()
~~~
