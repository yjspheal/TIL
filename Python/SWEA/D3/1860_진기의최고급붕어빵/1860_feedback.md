# 기존 코드
~~~python
# 1860. 진기의 최고급 붕어빵

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())     # N명의 손님, M초마다 K개의 붕어빵 생성
    visitor_list = [0] * 11112      # 각 초에 손님이 몇명 오는지 저장할 리스트. 초는 11111 이하이다.
    latest_time = 0     # 젤 늦게 오는 손님 초 저장할 변수

    for visit_time in map(int, input().split()):    # 인풋받은 걸 하나씩 순회하며
        visitor_list[visit_time] += 1       # 해당 시간에 손님이 한명 왔다

        if visit_time > latest_time:        # 젤 늦은 시간 update
            latest_time = visit_time

    current_boong = 0   # 현재 붕어빵 재고

    result = 'Possible' # 붕어빵 제공 가능 여부
    # 각 초별로 붕어빵 재고 파악
    for i in range(latest_time + 1):    # 제일 늦게오는 사람 초까지만 보면 됨
        if i > 0 and i % M == 0:      # M초마다 붕어빵 K개 생성
            current_boong += K

        current_boong -= visitor_list[i]    # 지금 온 손님에게 하나씩 주기
        if current_boong < 0:       # 붕어빵 재고보다 더 줘야되는 상황이었으면
            result = 'Impossible'       # 불가능

    print(f'#{tc} {result}')
~~~
<br><br>


# 총평
- “i초마다 생산량 = (i>0 and i%M==0)*K”와 “해당 초 방문자 수만큼 소진” 아이디어로 올바르게 시뮬레이션되어 있습니다.
- 다만 최대 초를 11,111로 가정한 고정 크기 배열은 **불필요한 메모리/시간 낭비** 가능성이 있고, 입력 제약이 바뀌면 취약합니다.
- `result`가 이미 `'Impossible'`이어도 루프를 계속 도는 점은 **조기 종료로 최적화**할 수 있습니다.
- 더 간결하고 빠른 표준 풀이가 있습니다: **도착 시간을 정렬**하여 손님 k번째가 시간 t에 왔을 때, 그때까지 생산된 붕어빵이 `(t // M) * K`개인지 비교하는 방식(O(N log N)). 구현 단순, 경계(0초 손님)도 자연 처리됩니다.
<br><br>


# 보완점
## 1. 정렬 기반 O(N log N) 검증으로 단순화
- 손님 도착 시각 배열 `arrivals`를 정렬.
- k번째(1-based) 손님이 `t`에 도착했다면, 그때까지 만든 빵은 `(t // M) * K`.
- 조건: `(t // M) * K >= k`가 모든 k에 대해 성립해야 `Possible`. 하나라도 깨지면 즉시 `Impossible`.
~~~python
arrivals.sort()
for k, t in enumerate(arrivals, start=1):
    if (t // M) * K < k:
        return "Impossible"
return "Possible"
~~~


<br><br>


## 2. 현재 방식 유지 시 개선 포인트
- 방문 배열은 **가변 길이**로 만들고, `latest_time` 계산 후 그 길이로 재구성하면 안전합니다.
- `result`가 `Impossible`이 되는 즉시 `break`로 **조기 종료**하세요.
~~~python
# latest_time 구한 뒤
visitor = [0] * (latest_time + 1)
for t in arrivals:
    visitor[t] += 1

stock = 0
result = "Possible"
for i in range(latest_time + 1):
    if i and i % M == 0:
        stock += K
    stock -= visitor[i]
    if stock < 0:
        result = "Impossible"
        break
~~~


<br><br>


# 최종 코드 예시
~~~python
# 1860. 진기의 최고급 붕어빵 - 정렬 기반 풀이 (권장)

from typing import List

def possible(N: int, M: int, K: int, arrivals: List[int]) -> str:
    """
    k번째(1-based) 손님이 시간 t에 도착했을 때,
    그때까지의 총 생산량 (t // M) * K 가 k 이상이어야 모두에게 제공 가능.
    0초 도착 손님은 생산 전이므로 자연스럽게 불가 처리됨.
    """
    arrivals.sort()
    for k, t in enumerate(arrivals, start=1):
        if (t // M) * K < k:
            return "Impossible"
    return "Possible"

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        N, M, K = map(int, input().split())
        arrivals = list(map(int, input().split()))
        print(f'#{tc} {possible(N, M, K, arrivals)}')

if __name__ == "__main__":
    main()
~~~
