# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")

# 동일한 글자를 지우는 함수 생성
def remove_same_char(chars):
    char_stack = []

    # stack에 원소를 하나씩 쌓으며 동일한지 확인
    for char in chars:
        # stack이 비어있거나, 마지막값이 현재 글자와 서로 다르면
        if not char_stack or char_stack[-1] != char:
            char_stack.append(char)
        
        # 마지막값 == 현재 글자면
        else:
            # 마지막 값 없애기
            _ = char_stack.pop()

    return char_stack

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 문자열 input
    sentence = input().strip()

    # 동일 문자열 삭제
    removed_sentence = remove_same_char(sentence)
    
    print(f'#{test_case} {len(removed_sentence)}')