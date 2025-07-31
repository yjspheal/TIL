# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
# 여러 개의 테스트 케이스를 순서대로 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    # 문자열 한 줄을 그대로 읽어서 각 문자를 int로 변환해 리스트로 만듭니다.
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 1) 출발점(2)의 좌표를 찾습니다.
    sx = sy = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sx, sy = i, j
                break
        if sx != -1:
            break

    # 2) BFS용 큐를 리스트로 구현합니다.
    queue = [(sx, sy)]
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True

    reachable = 0
    # 3) 큐에 남은 좌표가 있으면 꺼내서 네 방향을 탐색
    while queue:
        x, y = queue.pop(0)  # 맨 앞에서 꺼냄
        # 도착점(3)을 만나면 바로 1을 반환
        if maze[x][y] == 3:
            reachable = 1
            break
        # 상하좌우로 이동
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            # 미로 범위 내, 방문하지 않았고 벽(1)이 아니면 이동
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and maze[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    print(f"#{tc} {reachable}")