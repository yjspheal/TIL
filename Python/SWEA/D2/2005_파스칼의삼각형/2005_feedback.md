# 기존 코드
~~~python
# 2005_파스칼의삼각형.파스칼의 삼각형
# 풀긴 풀었으나 N이 커지면 메모리 초과될듯. pop하는 과정이 없어 stack이 아닌듯한..

T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input())  # 파스칼의 삼각형 줄 수

    stack = [1]  # 스택 초기화, 첫줄은 1
    pointer = 0  # 더해야 할 윗줄 원소의 인덱스

    # 출력 시작
    print(f'#{tc}')
    print(*stack)  # 1

    # 파스칼의 삼각형 각 줄을 돌며
    for row in range(1, N):  # 첫 줄은 이미 채웠으므로
        stack.append(1)  # 맨 처음 값은 1로 고정이므로 1을 추가
        pointer += 1  # 윗윗줄 마지막에 위치하던 포인터를 윗줄 첫번째로 옮겨준다

        for _ in range(1, row):  # 맨 마지막 값도 1로 고정이므로, 양쪽 범위를 뺀다
            stack.append(stack[pointer] + stack[pointer + 1])  # 현재 포인터가 위치한 원소와 그 다음 원소를 더한다
            pointer += 1  # 포인터를 하나 옮겨준다

        stack.append(1)  # 맨 마지막 값 추가


        # 이번 줄을 출력한다
        print(*stack[(row * (row + 1)) // 2:])
~~~
<br><br>


# 총평
- 아이디어는 “윗줄의 인접한 두 수를 더해 다음 줄을 만든다”로 맞습니다.
- 다만 현재 구현은 한 리스트에 모든 원소를 **평면(1차원)으로 누적**해 두고, 그 위를 `pointer`로 더해 가는 방식인데, 계산에 **방금 append한 ‘현재 줄’ 값이 섞여 들어가** 잘못된 결과가 나옵니다(예: N=4일 때 `1 3 2 1` 출력).
- 또한 모든 줄을 한 리스트에 누적하므로 **메모리 사용이 O(N²)** 입니다. N이 커지면 메모리/시간 모두 비효율적입니다.
- 이 문제는 스택이 없어도 되며, 한 줄만 유지하는 **O(N) 메모리, in-place 업데이트** 방식이 간단하고 빠릅니다.
<br><br>


# 보완점
## 1. 알고리즘 버그(포인터가 현재 줄을 참조) 수정
현재 로직은 `stack.append(...)`로 “현재 줄”에 값을 추가하면서, 곧바로 `stack[pointer] + stack[pointer + 1]`을 계산합니다. 이때 `pointer`가 이전 줄만 가리킨다는 보장이 없어 **동일 줄에서 방금 추가한 값**을 참조하는 문제가 발생합니다.  
해결책은 두 가지입니다.
- (권장) **이전 줄을 별도 리스트로 유지**하여 그로부터만 합을 계산
- (가능) 1차원 평면 저장을 고수하려면, **“이전 줄의 시작/끝 인덱스”를 명시적 계산**으로 참조

예: 이전 줄 시작/끝 인덱스
~~~python
# r번째 줄(0-based)을 만들 때, 이전 줄은 (r-1)번째 줄
prev_start = (r-1)*r//2          # 이전 줄 시작 인덱스
# 이전 줄 길이는 r, 끝 인덱스는 prev_start + r - 1
# 새 줄의 가운데 값은 for j in range(r-1): stack[prev_start+j] + stack[prev_start+j+1]
~~~

<br><br>


## 2. 메모리 O(N)로 최적화 (in-place, 오른쪽→왼쪽 업데이트)
파이썬의 리스트 하나만으로 각 줄을 **오른쪽에서 왼쪽으로** 갱신하면, 현재 줄 계산 시 이전 값이 덮어쓰여도 참조 안전성을 유지할 수 있습니다.
~~~python
row = []
for i in range(N):        # i번째 줄을 만든다 (0-based)
    row.append(1)         # 맨 오른쪽에 1 추가
    for j in range(i-1, 0, -1):
        row[j] = row[j] + row[j-1]   # 중앙부 갱신(오른쪽→왼쪽)
    print(*row)
~~~
- 공간: 최대 길이 N의 한 줄만 유지 → **O(N)**
- 시간: 전체적으로 여전히 O(N²) (파스칼 자체가 그렇게 큼)

<br><br>


## 3. 조합식(nCk)로 직접 생성 (정확, 깔끔)
각 줄 r에서 항들을 `C(r,k)`로 바로 생성할 수도 있습니다. 인접 항의 비율을 이용하면 부동소수점 없이 정수로 안전하게 갱신됩니다.
~~~python
def pascal_row(r: int):
    # r번째 줄(0-based) 0..r
    c = 1
    yield c
    for k in range(r):
        c = c * (r - k) // (k + 1)   # C(r,k+1) = C(r,k) * (r-k)/(k+1)
        yield c
~~~
- 파이썬은 임의 정밀도 정수이므로 오버플로우 걱정 없음.
- 매 줄을 즉시 출력하고 버리면 메모리 O(N).

<br><br>


# 최종 코드 예시
~~~python
# O(N) 메모리, in-place 오른쪽→왼쪽 갱신 방식

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    row = []
    for i in range(N):             # i: 0..N-1
        row.append(1)              # 양 끝은 1
        # 중앙부를 오른쪽→왼쪽으로 갱신하여 이전 값 참조 안전성 보장
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
        print(*row)
~~~
