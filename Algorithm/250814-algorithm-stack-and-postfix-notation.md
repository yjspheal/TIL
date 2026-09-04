- [스택 (Stack)](#스택-stack)
- [후위 표기법 (Postfix Notation)](#후위-표기법-postfix-notation)
  - [개념](#개념)
  - [후위 표기법의 장점](#후위-표기법의-장점)
  - [후위 표기법 계산 알고리즘 (스택 활용)](#후위-표기법-계산-알고리즘-스택-활용)
  - [Python 예시](#python-예시)

---

## 스택 (Stack)

- 데이터의 입출력이 한쪽 끝에서만 일어나는 **후입선출(LIFO, Last-In, First-Out)** 방식의 자료구조.
- 가장 마지막에 추가된 데이터가 가장 먼저 제거된다.
- 주요 연산: `push` (데이터 추가), `pop` (데이터 제거), `peek` (가장 위의 데이터 확인).

---

## 후위 표기법 (Postfix Notation)

### 개념
- 연산자를 피연산자 뒤에 위치시키는 표기법. (예: `3 4 +`)
- 컴퓨터가 수식을 계산할 때 괄호나 연산자 우선순위를 고려할 필요가 없어 매우 효율적이다.
- **중위 표기법 (Infix Notation)**: `3 + 4` (사람이 사용하는 일반적인 표기법)
- **전위 표기법 (Prefix Notation)**: `+ 3 4`

### 후위 표기법의 장점
- 괄호가 필요 없다.
- 연산자의 우선순위를 고려할 필요가 없다.
- 수식을 왼쪽에서 오른쪽으로 한 번만 읽으면 계산이 가능하다.

### 후위 표기법 계산 알고리즘 (스택 활용)
1.  수식을 왼쪽부터 차례로 읽는다.
2.  **피연산자(숫자)**가 나오면 스택에 `push`한다.
3.  **연산자**가 나오면 스택에서 피연산자 두 개를 `pop`한다.
    - (주의: 먼저 `pop`된 것이 두 번째 피연산자, 나중에 `pop`된 것이 첫 번째 피연산자이다.)
4.  두 피연산자를 가지고 해당 연산을 수행하고, 그 결과를 다시 스택에 `push`한다.
5.  수식의 끝까지 이 과정을 반복한다.
6.  최종적으로 스택에 남아있는 하나의 값이 수식의 결과이다.

### Python 예시
```python
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        # 토큰이 숫자인지 확인
        if token.isdigit():
            stack.append(int(token))
        # 연산자인 경우
        else:
            # 스택에서 피연산자 두 개를 꺼냄
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                # 나눗셈은 정수 나눗셈으로 처리
                stack.append(operand1 // operand2)

    return stack.pop()

# 예시: "7 2 + 4 * 5 -"
# 1. 7, 2 push -> stack: [7, 2]
# 2. + -> 7+2=9, 9 push -> stack: [9]
# 3. 4 push -> stack: [9, 4]
# 4. * -> 9*4=36, 36 push -> stack: [36]
# 5. 5 push -> stack: [36, 5]
# 6. - -> 36-5=31, 31 push -> stack: [31]
# 결과: 31

expression = "7 2 + 4 * 5 -"
result = evaluate_postfix(expression)
print(f'후위 표기법 "{expression}"의 계산 결과: {result}') # 31
```
