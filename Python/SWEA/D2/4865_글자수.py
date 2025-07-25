# [파이썬 S/W 문제해결 기본] 3일차 - 글자수


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()  # 길이가 N인 문자열 1
    str2 = input()  # 길이가 M인 문자열 2


    # str2에 들어있는 문자별 갯수를 저장할 dict 초기화
    char_dict = {}
    
    for char2 in str2:
        if char2 in str1:   # str1에 들어있던 문자에 대해서만 딕셔너리에 추가
            try:
                char_dict[char2] += 1
            except:
                char_dict[char2] = 1    # 값이 없었으면 1으로 생성
        else:
            pass        # str1에 없었으면 pass

    # max_char = max(char_dict, key = lambda x: char_dict[x])
    
    print(f'#{test_case} {max(char_dict.values())}')