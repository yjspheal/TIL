import sys

sys.stdin = open('input.txt')


def my_push(item):
    global stack, top

    top += 1  # 하나 더해주므로 top + 1
    stack[top] = item  # item 넣어주기


def my_pop():
    global stack, top

    if top == -1:
        return

    top -= 1  # 하나 뺄 것므로 top -1
    return stack[top + 1]  # top + 1 하여 return


T = int(input())  # 테스트케이스 수
for tc in range(1, T + 1):
    brackets = input().strip()  # 소괄호로만 이루어진 문자열

    stack = [0] * 10  # 스택 정의
    top = -1  # top 초기화

    is_valid = 1

    for bracket in brackets:
        if bracket == '(':
            my_push('(')
        else:
            result = my_pop()

            if not result:  # pop 결과가 none이면 스택에 여는 괄호가 없었다는 뜻
                is_valid = -1
                break

    if top > -1:  # for문이 끝났는데 stack이 남아있다면
        is_valid = -1

    print(f'#{tc} {is_valid}')
