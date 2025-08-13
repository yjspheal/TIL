def my_push(item):
    global stack, top

    top += 1  # 하나 더해주므로 top + 1
    stack[top] = item  # item 넣어주기


def my_pop():
    global stack, top

    top -= 1  # 하나 뺄 것므로 top -1
    return stack[top + 1]  # top + 1 하여 return


size = 10               # size 지정
stack = [0] * size          # 스택 생성

top = -1                # top 초기화

# push 3번
for i in range(1, 4):
    my_push(i * 100)

# pop 3번
for _ in range(3):
    print(my_pop())
