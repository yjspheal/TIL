# by gpt

from collections import deque

# 8방향
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

def count_mines(board, x, y, N):
    cnt = 0
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if in_range(nx, ny, N) and board[nx][ny] == '*':
            cnt += 1
    return cnt

def bfs(x, y, board, visited, mine_cnt, N):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        if mine_cnt[cx][cy] == 0:
            for d in range(8):
                nx, ny = cx + dx[d], cy + dy[d]
                if in_range(nx, ny, N) and not visited[nx][ny] and board[nx][ny] == '.':
                    visited[nx][ny] = True
                    if mine_cnt[nx][ny] == 0:
                        q.append((nx, ny))  # 다시 확장
                    # 숫자칸도 방문 표시 필요 (연쇄 중 열리므로)

def solve(N, board):
    visited = [[False]*N for _ in range(N)]
    mine_cnt = [[0]*N for _ in range(N)]

    # Step 1: 각 칸 주변 지뢰 수 세기
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                mine_cnt[i][j] = count_mines(board, i, j, N)

    clicks = 0

    # Step 2: 0인 칸부터 BFS로 연쇄 열기
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and not visited[i][j] and mine_cnt[i][j] == 0:
                bfs(i, j, board, visited, mine_cnt, N)
                clicks += 1

    # Step 3: 여전히 안 열린 칸(숫자칸)은 개별 클릭 필요
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and not visited[i][j]:
                clicks += 1

    return clicks

# 입력 처리
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    ans = solve(N, board)
    print(f"#{t} {ans}")
