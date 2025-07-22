import sys
sys.stdin = open("input.txt", "r")

def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

def rotate_270(matrix):
    return [list(col) for col in zip(*matrix)][::-1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]

    rot90 = rotate_90(matrix)
    rot180 = rotate_180(matrix)
    rot270 = rotate_270(matrix)

    print(f"#{test_case}")
    for i in range(N):
        r90 = ''.join(rot90[i])
        r180 = ''.join(rot180[i])
        r270 = ''.join(rot270[i])
        print(f"{r90} {r180} {r270}")
