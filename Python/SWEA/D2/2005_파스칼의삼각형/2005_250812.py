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
