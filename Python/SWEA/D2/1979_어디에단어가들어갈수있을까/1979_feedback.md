# 기존 코드
~~~python
# 1979. 어디에 단어가 들어갈 수 있을까

# import sys
#
# sys.stdin = open('input.txt')


def count_K_length_word(arr, k):
    """
    arr의 각 줄을 돌며, 연속되는 1의 갯수가 정확히 k개인 것의 갯수를 세서 return
    Args:
        arr (list): 0 또는 1을 원소로 갖는 이차원 배열
        k (int): 타겟 길이
    Returns:
        int: 연속되는 1의 길이가 k인 것의 갯수
    """

    k_count = 0  # k인 단어 갯수
    n = N  # 한 줄당 길이

    for line in arr:  # arr의 각 줄을 돌며
        current_length = 0  # 현재 연속되는 1의 길이

        for i, ele in enumerate(line):  # 각 줄의 원소를 돌며
            if ele == 1:  # 흰색이면
                current_length += 1  # 현재 길이에 1을 늘린다

            if ele == 0 or i == n - 1:  # 검정색이거나, 마지막이라면
                if current_length == k:  # 현재 길이가 정확히 k라면
                    k_count += 1  # k인 단어 갯수에 1을 늘린다

                current_length = 0  # 길이 초기화

    return k_count


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    crossword = [list(map(int, input().split())) for _ in range(N)]  # 단어퍼즐 정보
    crossword += list(map(list, zip(*crossword)))

    result = count_K_length_word(crossword, K)

    print(f'#{tc} {result}')
~~~
<br><br>


# 총평
- 전체 로직은 “가로/세로 각각의 줄에서 연속된 1의 길이가 정확히 K인 구간 개수”를 세는 문제 의도에 맞게 구현되었습니다.
- 전치(`zip(*crossword)`)를 이용해 한 번의 함수로 가로/세로를 함께 처리한 접근이 깔끔합니다.
- 다만, `count_K_length_word()`가 전역 변수 `N`에 의존합니다. 함수 정의 시점엔 `N`이 없고, 호출 시점에만 존재하므로 **전역 의존**을 제거하는 편이 안전합니다.
- 마지막 원소 처리 위해 `i == n - 1`로 분기하는 방식은 동작은 맞지만, **센티넬(끝에 0 하나 추가)** 기법을 쓰면 분기가 단순해집니다.
- 변수/타입 힌트, 메인 함수 분리 등으로 가독성과 제출 안정성을 더 높일 수 있습니다.
<br><br>


# 보완점
## 1. 전역 의존 제거 (`N` 참조)
- 함수 내부에서 행 길이를 직접 쓰면 전역 `N` 참조가 필요 없습니다.
- 더 나아가 센티넬 방식이면 길이 참조조차 필요 없습니다.

~~~python
def count_K_length_word(lines, k):
    count = 0
    for line in lines:
        run = 0
        for v in line + [0]:      # 센티넬 0 추가
            if v == 1:
                run += 1
            else:
                if run == k:
                    count += 1
                run = 0
    return count
~~~


<br><br>


## 2. 전치 처리 명확화 및 메모리 관점
- `crossword += list(map(list, zip(*crossword)))`는 원본 리스트에 전치된 “새 행들”을 이어 붙입니다. 의도는 정확합니다.
- 가독성을 위해 변수로 분리해 두 단계로 작성하면 디버깅이 쉬워집니다. (메모리 사용은 동일 수준)
~~~python
cols = [list(col) for col in zip(*crossword)]
all_lines = crossword + cols
result = count_K_length_word(all_lines, K)
~~~


<br><br>


## 3. I/O 및 구조화 (제출 안정성)
- 메인 블록을 함수로 분리하고 타입 힌트를 추가하면 유지보수성이 좋아집니다.

~~~python
from typing import List

def main() -> None:
    T = int(input())
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        grid: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]
        cols = [list(col) for col in zip(*grid)]
        print(f'#{tc} {count_K_length_word(grid + cols, K)}')

if __name__ == "__main__":
    main()
~~~


<br><br>


# 최종 코드 예시
~~~python
# 1979_어디에 단어가 들어갈 수 있을까

from typing import List

def count_K_length_word(lines: List[List[int]], k: int) -> int:
    """
    각 줄(가로/세로)에서 '연속된 1의 길이 == k' 인 구간의 개수를 합산해 반환.
    센티넬 0을 덧붙여 마지막 구간 처리 분기를 단순화한다.
    """
    count = 0
    for line in lines:
        run = 0
        for v in line + [0]:  # 센티넬
            if v == 1:
                run += 1
            else:
                if run == k:
                    count += 1
                run = 0
    return count


def main() -> None:
    T = int(input())
    
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        
        grid: List[List[int]] = [list(map(int, input().split())) for _ in range(N)]
        
        cols = [list(col) for col in zip(*grid)]   # 전치(세로 줄)
        all_lines = grid + cols                    # 가로 + 세로
        
        result = count_K_length_word(all_lines, K)
        
        print(f'#{tc} {result}')

if __name__ == "__main__":
    main()
~~~
