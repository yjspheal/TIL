# 기존 코드
~~~python
# 22375_스위치조작. 스위치 조작

# import sys
# 
# sys.stdin = open('switch_sample_in.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 스위치 갯수

    start_lights = list(map(int, input().split()))  # 시작 전구 배열
    target_lights = list(map(int, input().split()))  # 목표 전구 배열

    switch_time = 0  # 지금까지 바뀐 횟수

    # 인덱스를 돌며
    for i in range(N):
        # 지금 전구 상태 = 시작 전구 상태 + 바꾼 횟수 를 2로 나눈 나머지(0 or 1이므로)
        c_light = (start_lights[i] + switch_time) % 2

        t_light = target_lights[i]  # 타겟 전구

        if c_light != t_light:  # 서로 다르면
            switch_time += 1  # 바꾼 횟수 + 1

    print(f'#{tc} {switch_time}')
~~~
<br><br>


# 총평
- 그리디 아이디어가 정확합니다: 앞에서부터 보며 현재까지의 토글 누적(홀/짝)에 따라 현재 전구 상태를 계산하고, 목표와 다르면 토글 1회.
- 연산은 **XOR**로 표현하면 더 명확하고 빠릅니다. `a ^ b`는 2로 나눈 나머지 대신 비트 토글 의미가 직관적입니다.
- 입출력은 대량 데이터 대비 `sys.stdin.readline`이 안전합니다. 또한 `N`은 검증 외에는 직접 쓰지 않으므로 `zip` 순회로 간결화할 수 있습니다.
<br><br>


# 보완점
## 1. 모듈러(%) 대신 XOR로 토글 표현
- 현재 상태 `current = start ^ parity` 로 계산하고, 목표와 다르면 `parity ^= 1` 및 `answer += 1`.
~~~python
parity = 0
ans = 0
for s, t in zip(start_lights, target_lights):
    if (s ^ parity) != t:
        parity ^= 1
        ans += 1
~~~

<br><br>

<br><br>


# 최종 코드 예시
~~~python
# 22375_스위치조작. 스위치 조작
# 앞에서 i번째 스위치를 누르면 i번째부터 끝까지 토글됨.
# 최솟값은 앞에서부터 보며 현재까지의 토글 누적(parity)을 추적하는 그리디로 구한다.

import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        _ = int(input().strip())  # N(길이) — zip 순회로 대체하므로 값 자체는 쓰지 않음
        start = list(map(int, input().split()))
        target = list(map(int, input().split()))

        parity = 0  # 지금까지의 토글 횟수의 홀짝(0: 짝수, 1: 홀수)
        presses = 0

        for s, t in zip(start, target):
            # 현재 전구 상태 = 시작 상태 ^ parity
            if (s ^ parity) != t:
                # 목표와 다르면 현재 위치에서 스위치를 눌러 이후를 모두 토글
                parity ^= 1
                presses += 1

        print(f"#{tc} {presses}")

if __name__ == "__main__":
    solve()
~~~
