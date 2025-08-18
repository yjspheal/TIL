def infix_to_postfix(expression):
    # 각 연산자의 우선순위를 딕셔너리로 정의
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    # 연산자를 임시로 저장한 스택 정의
    stack = []
    # 최종 후위표기법 결과를 담을 리스트 정의
    result = []

    # 입력된 중위 표기법 식을 토큰 단위로 반복
    for token in expression:
        # 1. 피연산자(숫자나 문자)일 경우
        # if token not in '+-*/()':   # 이렇게 해도 되고
        if token.isalnum():  # 숫자나 문자면
            result.append(token)  # 바로 결과에 추가

        # 2. 여는 괄호 (는 무조건 스택에 push
        elif token == '(':
            stack.append(token)

        # 3. 닫는 괄호 )는 왼쪽 괄호 (를 만나기 전까지 pop하여 출력
        # (는 pop하되 출력은 하지 않음
        elif token == ')':

            # stack이 비어있지 않으며, stack의 top이 여는 괄호가 나올 때까지
            while stack and stack[-1] != '(':
                result.append(stack.pop())

            if stack:  # stack이 비어있지 않다면. 근데 닫는 괄호가 있는데 여는 괄호가 없을리가?
                stack.pop()  # top이 (이므로 pop만

        # 4. 연산자는 스택 top의 요소(isp) 와 본인(icp)의 우선순위를 비교하여
        # 본인 우선순위가 더 높을 때까지 top을 pop하여 출력
        # 더 높아지면 자기를 push
        else:
            # 스택 top의 연산자 우선순위(isp)와 현재 연산자 우선순위(icp)를 비교하여
            # 스택이 비어있지 않고, top이 여는 괄호가 아니며,
            # isp가 icp보다 높거나 같으면 계속 pop
            while (
                    stack
                    and stack[-1] != '('
                    and precedence.get(stack[-1], 0) >= precedence.get(token, 0)  # 0 넣는 건 필수가 아님
            ):
                result.append(stack.pop())

            # 그럼 이제 top의 isp는 토큰의 icp보다 낮은 것
            # push하기
            stack.append(token)

    # 5. 모든 입력을 처리한 후, 스택에 남은 연산자를 모두 pop하여 출력
    while stack:
        result.append(stack.pop())

    return ''.join(result)


# 테스트
expr1 = '(A+B)*C'
expr2 = '(A+B)*(C-D)'
print(infix_to_postfix(expr1))  # "AB+C*"
print(infix_to_postfix(expr2))  # "AB+CD-*"
