- [기존 코드](#기존-코드)
- [총평](#총평)
- [보완점](#보완점)
  - [1. 불필요 변수 제거](#1-불필요-변수-제거)
  - [2. 함수 간소화](#2-함수-간소화)
- [최종 코드 예시](#최종-코드-예시)


# 기존 코드
~~~python
# 1215_회문1. [S/W 문제해결 기본] 3일차 - 회문1

# import sys
#
# sys.stdin = open("input.txt")


def is_palindrome(char_list):
    """
    char_list 문자열 리스트에 대해, 회문인지 판단하여 맞다면 True 아니면 False를 반환하는 함수
    """

    return char_list == char_list[::-1]


T = 10
for tc in range(1, T + 1):
    M = int(input())  # 찾아야하는 회문의 길이
    sentences = [list(input()) for _ in range(8)]  # 8x8의 글자판이 주어진다
    sentences += list(zip(*sentences))  # 세로줄을 추가한다

    len_sentences = len(sentences)  # 16으로 고정이지만 그냥 계산
    len_row = len(sentences[0])  # 8로 고정이지만 그냥 계산

    count = 0  # 회문 갯수 계산
    for row in sentences:
        for i in range(len_row - M + 1):  # + M-1까지 회문인지 체크
            if is_palindrome(row[i: i + M]):        # 회문이라면 count + 1
                palindrome = row[i: i + M]
                count += 1

    print(f'#{tc} {count}')
~~~
<br><br>


# 총평
- 가로/세로를 합쳐서 한 번에 탐색하는 아이디어는 효율적이며 깔끔합니다.
- `is_palindrome`을 별도 함수로 분리해 가독성을 높인 점도 좋습니다.
- 다만, `palindrome = row[i: i + M]` 변수는 사용되지 않으므로 불필요합니다.
- `len_sentences`는 이후에 사용되지 않으니 제거 가능.
- `zip(*sentences)`로 세로줄을 추가하면 세로줄 데이터가 tuple 형태가 되는데, 여기서는 비교에 문제는 없지만 통일성을 위해 list 변환하는 것이 좋습니다.
<br><br>


# 보완점
## 1. 불필요 변수 제거
- 사용되지 않는 `palindrome`과 `len_sentences` 삭제.
- `list(zip(*sentences))`를 `map(list, zip(*sentences))`로 바꾸면 행 타입이 통일됩니다.

## 2. 함수 간소화
- `is_palindrome` 함수는 단일 구문이라 inline으로 사용 가능.
- 또는 그대로 두더라도 docstring과 함께 명확히 유지 가능.

<br><br>


# 최종 코드 예시
~~~python
# 1215. 회문1

def is_palindrome(seq) -> bool:
    """시퀀스가 회문인지 여부 반환"""
    return seq == seq[::-1]

def main() -> None:
    T = 10
    for tc in range(1, T + 1):
        M = int(input())
        grid = [list(input().strip()) for _ in range(8)]
        # 가로 + 세로
        lines = grid + list(map(list, zip(*grid)))

        count = 0
        for row in lines:
            for i in range(8 - M + 1):
                if is_palindrome(row[i:i + M]):
                    count += 1
        print(f'#{tc} {count}')

if __name__ == "__main__":
    main()
~~~
