# TIL - 2025-07-XX

- [KMP 알고리즘](#kmp-알고리즘)
- [보이어-무어 알고리즘](#보이어-무어-알고리즘)

---

## KMP 알고리즘

### 개념
- **Knuth-Morris-Pratt (KMP)** 알고리즘은 문자열 검색 알고리즘으로, 불필요한 비교를 줄여 **O(n + m)** 시간에 패턴 검색을 수행.
- 부분 일치 테이블(파이 접두사/접미사 배열)을 만들어, 불일치 발생 시 **이전까지의 비교 정보를 재활용**.

### 동작 원리
1. **부분 일치 테이블(LPS, Longest Prefix Suffix)** 생성
    - 패턴의 각 위치에서 접두사와 접미사가 일치하는 최대 길이를 기록
2. 본문 문자열을 순차 탐색
    - 불일치 발생 시, LPS 테이블을 참고하여 패턴 이동
    - 이미 일치한 부분은 재비교하지 않음

### 시간복잡도
- 전처리(LPS 생성): O(m)
- 검색: O(n)
- 총합: O(n + m)  
  (n: 본문 길이, m: 패턴 길이)

### 장점
- 항상 O(n + m) 시간 보장
- 불필요한 재탐색 최소화

### 단점
- LPS 테이블 생성 과정 이해가 어렵다
- 실제 평균 검색 속도는 보이어-무어보다 느릴 수 있음

### 활용 사례
- DNA 서열, 로그 파일, 대규모 텍스트에서 특정 패턴 검색

### Python 예시
~~~python
def kmp_search(text, pattern):
    def build_lps(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print(f"패턴 발견 위치: {i-j}")
            j = lps[j-1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
~~~

---

## 보이어-무어 알고리즘

### 개념
- **Boyer-Moore** 알고리즘은 문자열 검색 시 **오른쪽→왼쪽**으로 패턴을 비교하며, 불일치 시 최대한 멀리 패턴을 이동.
- **Bad Character Rule**과 **Good Suffix Rule** 두 가지 규칙을 사용.

### 동작 원리
1. 패턴을 본문에 맞춰서 오른쪽부터 비교
2. 불일치 발생 시:
   - **Bad Character Rule**: 불일치 문자가 패턴에 존재하는 가장 오른쪽 위치로 패턴 이동
   - **Good Suffix Rule**: 이미 일치한 접미사와 일치하는 다른 접미사를 찾아 패턴 이동
3. 두 규칙 중 더 많이 이동할 수 있는 값을 선택

### 시간복잡도
- 최악: O(nm)
- 평균: 매우 빠름 (n/m 수준)
- 특히 알파벳 종류가 많고, 패턴 길이가 긴 경우 성능 우수

### 장점
- 실제 평균 검색 속도가 매우 빠름
- 불필요한 비교 최소화

### 단점
- 구현 복잡
- 최악의 경우 O(nm) 발생 가능 (ex. 패턴과 본문이 거의 같은 경우)

### 활용 사례
- 대규모 텍스트 검색
- 검색 엔진, 문자열 편집기(find 기능) 등

### Python 예시 (Bad Character Rule 기반)
~~~python
def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    # Bad character 테이블 생성
    bad_char = {c: -1 for c in set(text)}
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0  # shift
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"패턴 발견 위치: {s}")
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

boyer_moore_search("ABAAABCD", "ABC")
~~~
