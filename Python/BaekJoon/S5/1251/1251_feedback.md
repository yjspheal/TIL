# 기존 코드
~~~python
# 1251 단어 나누기

import sys

input = sys.stdin.readline

"""
단어를 3개로 쪼갠다
3개의 단어를 reverse한다
다시 붙인다
이런 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 만드시오

1. 인덱스 N-3까지 ord가 제일 작은 문자를 찾는다
2. 그걸로 뒤집는다
3. 인덱스 N-2까지...반복
"""


def find_earlist_char_idx(sentence, start_idx, end_idx):
    """
    sentence[start_idx: end_idx]에서, 가장 사전적으로 먼저 오는 문자의 인덱스를 반환한다.

    Args:
        sentence (char): 인자로 받을 문자열
        start_idx (int): sentence에서 인덱스 따질 범위 시작점
        end_idx (int): sentence에서 인덱스 따질 범위 끝점

    Returns:
        int: 사전적으로 제일 빠른 문자 인덱스
    """
    min_ord = ord(sentence[start_idx])
    min_idxs = []

    for i, char in enumerate(sentence):
        if start_idx <= i < end_idx:  # 범위에 들어와야 계산

            if ord(char) < min_ord:  # 최소값 갱신 시 update
                min_ord = ord(char)
                min_idxs = [i]

            elif ord(char) == min_ord:  # 똑같다면 추가
                min_idxs.append(i)

    return min_idxs


def is_earlier(arr1, arr2):
    """
    ord값 리스트 2개를 받아다가, 각 자리수별로 비교한 후
    arr2값이 arr1보다 작다면 True, 아니라면 False 반환

    Example:
        arr1 = [2, 4, 13, 42, 1]
        arr2 = [2, 4, 12, 44, 1]
        -> 12가 13보다 작으므로 return True
    """

    for i in range(len(arr1)):
        if arr2[i] < arr1[i]:   # 2가 더 작으면
            return True
        elif arr2[i] > arr1[i]:   # 2가 더 크면
            return False

    else:   # 모두 같았다면
        return False



def cal_ord(sentence):
    """
    sentence문자열을 돌며 각 ord값을 list형태로 반환
    """
    result = []
    for s in sentence:
        result.append(ord(s))

    return result


# 단어 입력
word = input().rstrip()
N = len(word)  # 단어 길이

ords = []

earlist_idxs = find_earlist_char_idx(word, 0, N - 2)
worst_char = 'z' * len(word)
min_ord = cal_ord(worst_char)     # 초기값은 최악 단어로.
result = worst_char

for flag1 in earlist_idxs:  # 일단 첫번쨰 flag는 최저값에서 찾아야함
    for flag2 in range(flag1 + 1, N - 1):  # 맨 마지막값은 빼야 단어길이 1 이상이 보장됨
        word1 = word[:(flag1 + 1)][::-1]  # 뒤집
        word2 = word[(flag1 + 1): (flag2 + 1)][::-1]
        word3 = word[(flag2 + 1):][::-1]

        new_word = word1 + word2 + word3
        new_word_ord = cal_ord(new_word)      # ord 배열 계산

        if is_earlier(min_ord, new_word_ord):       # new_word가 기존보다 더 빠르면
            min_ord = new_word_ord
            result = new_word

print(result)
~~~
<br><br>


# 총평
- 문제 의도(모든 분할(i, j)에 대해 뒤집고 사전순 최소)를 잘 파악하셨습니다.
- 다만 "첫 구간 시작은 가장 작은 문자 위치에서만" 탐색하는 그리디 가지치기는 **전역 최소를 보장하지 않습니다**. 반례가 존재할 수 있어요.
- `find_earlist_char_idx`(오타: earliest)의 반환 타입/설명이 불일치(문서엔 int, 실제 코드는 list)하며, 구현도 범위 전체를 매번 순회해 비효율적입니다.
- 파이썬은 **문자열 자체의 사전순 비교가 가능**하므로 `ord` 리스트로 변환해서 비교할 필요가 없습니다.
- 본 문제의 N≤50이므로 단순 이중 루프 O(N²)로 모든 분할을 생성한 뒤 `min`으로 고르는 게 가장 간단·안전·가독성 좋습니다.
<br><br>


# 보완점
## 1. 전역 최소 보장: 모든 분할을 고려
현재 코드는 첫 번째 컷 위치를 "가장 작은 문자 인덱스들"로 제한합니다. 하지만 두 번째/세 번째 조각의 뒤집힘 효과로 전체 문자열의 사전순이 뒤바뀔 수 있으므로, **모든 (i, j)** (0 ≤ i < j < N-1)을 순회해야 합니다.

~~~python
s = input().strip()
n = len(s)

best = min(
    s[:i+1][::-1] + s[i+1:j+1][::-1] + s[j+1:][::-1]
    for i in range(n - 2)
    for j in range(i + 1, n - 1)
)
print(best)
~~~

- 복잡도: O(N²)개의 후보 × 각 후보 생성 O(N) → O(N³)처럼 보이지만, N≤50이라 충분합니다.
- 파이썬의 문자열 비교는 사전순이 기본 동작이므로 `min`이 바로 최솟값을 줍니다.

<br><br>


## 2. 불필요한 보조 함수/구조 제거 및 네이밍/문서화 정리
- `cal_ord`, `is_earlier`, `find_earlist_char_idx`는 모두 불필요합니다. 문자열 직접 비교가 더 간단하고 안전합니다.
- 오타 수정(earlist → earliest), 반환 타입/설명 불일치 제거.
- 입출력은 백준 스타일로 최소화(`sys.stdin.readline` 유지 가능).

~~~python
import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    ans = min(
        s[:i+1][::-1] + s[i+1:j+1][::-1] + s[j+1:][::-1]
        for i in range(n - 2)
        for j in range(i + 1, n - 1)
    )
    print(ans)

if __name__ == "__main__":
    solve()
~~~

- 가독성을 위해 `solve()`로 분리했지만, 한 파일 한 함수 없이도 무방합니다.

<br><br>


# 최종 코드 예시
~~~python
# 1251 단어 나누기 - 모든 (i, j) 분할을 고려한 정석 풀이
import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)

    # 세 조각의 뒤집힌 합 중 사전순 최솟값을 직접 구한다.
    best = min(
        s[:i+1][::-1] + s[i+1:j+1][::-1] + s[j+1:][::-1]
        for i in range(n - 2)
        for j in range(i + 1, n - 1)
    )
    print(best)

if __name__ == "__main__":
    solve()
~~~
