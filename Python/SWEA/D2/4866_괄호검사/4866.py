# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

# import sys
# sys.stdin = open("sample_input.txt", "r")

# import re

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    sentence = input().strip()

    # sentence에서 ( ) { } 제외 모두 제거
    # compiler = re.compile('[{}()]')
    # blancket_list = compiler.findall(sentence)
    # 를 하려 하였으나 온라인저지에서 re모듈 사용 불가능하여 아래로 대체

    # 따라서 반복문으로 구현
    blancket_list = []
    for char in sentence:
        if char == '{' or char == '}' or char == '(' or char == ')':
            blancket_list.append(char)

    
    blancket_str = ''.join(blancket_list)   # 괄호만 남긴 문자열로 변환

    is_expression = 1
    while blancket_str: # 문자열이 남아있는 동안
        len_before = len(blancket_str)  # 제거 전 문자열 길이

        blancket_str = blancket_str.replace('{}', '') # 중괄호쌍이 정확히 붙어있으면 ok
        blancket_str = blancket_str.replace('()', '') # 소괄호쌍이 정확히 붙어있으면 ok

        len_after = len(blancket_str)  # 제거 후 문자열 길이

        # 만약 길이가 같다면(즉 아무것도 제거가 안 됐다면)
        if len_before == len_after:     
            # 문자열이 남아있는 상태로 반복문이 도므로, 잘못된 표현식이란 뜻
            is_expression = 0
            break


    
    print(f'#{test_case} {is_expression}')