import sys
sys.stdin = open("input.txt")

T = int(input())        # 테케 수
for tc in range(1, T+1):
    sentence = input()  # 문자열 입력
    # 자리 바꾸기
    reversed = ''
    # sentence에 문자가 남아있는 동안 계속 루프
    while True:
        reversed += sentence[-1]
        sentence = sentence[:-1]    # 마지막걸 떼어버림
        if not sentence:    # sentence가 다 없어지면 sentence는 False로 판단됨. not False == True
            break

    print(f'{tc} {reversed}')