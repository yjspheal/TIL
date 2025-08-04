- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요한 DP 테이블 제거](#1-불필요한-dp-테이블-제거)
  - [2. 반복 제거 및 메모리 절감](#2-반복-제거-및-메모리-절감)
  - [3. 순차적 토너먼트 시뮬레이션](#3-순차적-토너먼트-시뮬레이션)
  - [4. 승자 결정 로직 분리](#4-승자-결정-로직-분리)
- [최종 코드 예시](#최종-코드-예시)


<br><br>

# 총평
- 토너먼트 방식으로 카드게임 승자를 정확히 시뮬레이션함
- 분할 정복(DP) 접근을 사용해 모든 구간의 로그를 구성하여 최종 우승자를 도출함
- 가위바위보 승리 규칙(무승부 시 인덱스 비교 포함)을 올바르게 구현함

<br><br>

# 보완점
## 1. 불필요한 DP 테이블 제거
모든 구간([l, r])에 대해 로그를 저장하는 DP 방식은 메모리와 연산 비용이 과도하게 큽니다.
- DP 표 크기: \(O(N^2)\)
- 각 셀에서 리스트를 합치는 비용: 구간 길이에 비례하므로 전체 시간 \(O(N^3)\)까지 증가할 수 있습니다.

**개선안**: 오직 토너먼트 구조(고정된 분할)에 해당하는 구간만 재귀 또는 반복으로 처리하고, 각 단계에서 승자만 전달하세요.

<br><br>
## 2. 반복 제거 및 메모리 절감
현재 `dp[l][r] = left_log + right_log + [winner]` 형태로 모든 매치 로그를 저장하지만, 최종 우승자만 필요합니다.
- 로그 저장을 제거하고, 구간별 승자 인덱스만 반환하도록 수정하세요.

```python
# 재귀적 분할 정복 예시
def get_winner(cards, l, r):
    if l == r:
        return l
    mid = (l + r) // 2
    left = get_winner(cards, l, mid)
    right = get_winner(cards, mid+1, r)
    return decide_winner(left, right, cards)
```

<br><br>
## 3. 순차적 토너먼트 시뮬레이션
재귀 대신 리스트를 절반씩 줄여가며 반복 처리할 수도 있습니다.
```python
def play(cards):
    while len(cards) > 1:
        next_round = []
        for i in range(0, len(cards), 2):
            a, b = cards[i], cards[i+1]
            next_round.append(decide_winner(a, b))
        cards = next_round
    return cards[0]
```

<br><br>
## 4. 승자 결정 로직 분리
가위바위보 판정을 `decide_winner(a, b)` 함수로 추출해 재사용성과 가독성을 높이세요.
```python
def decide_winner(a, b):
    # a, b는 (인덱스+1)
    ca, cb = cards[a-1], cards[b-1]
    if ca == cb:
        return a if a < b else b
    wins = {(1,3), (2,1), (3,2)}
    return a if (ca, cb) in wins else b
```

<br><br>
# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

# 가위바위보 판정 맵
WINS = {(1,3), (2,1), (3,2)}

def decide_winner(idx_a, idx_b, lineup):
    a, b = lineup[idx_a], lineup[idx_b]
    if a == b:
        return idx_a if idx_a < idx_b else idx_b
    return idx_a if (a, b) in WINS else idx_b

# 재귀적 분할 정복
def tournament(lineup, l, r):
    if l == r:
        return l
    mid = (l + r) // 2
    left = tournament(lineup, l, mid)
    right = tournament(lineup, mid+1, r)
    return decide_winner(left, right, lineup)

if __name__ == '__main__':
    T = int(input().strip())
    for tc in range(1, T+1):
        N = int(input().strip())
        cards = list(map(int, input().split()))
        # 인덱스(0~N-1)로 처리
        champion_idx = tournament(cards, 0, N-1)
        # +1 하여 번호로 변환
        champion = champion_idx + 1
        print(f"#{tc} {champion}")
```  