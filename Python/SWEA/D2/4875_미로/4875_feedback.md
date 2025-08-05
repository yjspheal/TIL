- [총평](#총평)
- [보완점](#보완점)
  - [1. BFS/DFS 단순화 및 명확화](#1-bfsdfs-단순화-및-명확화)
  - [2. 전역 상태 제거 및 입력 분리](#2-전역-상태-제거-및-입력-분리)
  - [3. 가독성을 위한 자료구조와 변수명 정리](#3-가독성을-위한-자료구조와-변수명-정리)
- [최종 코드 예시](#최종-코드-예시)



<br>
<br>

# 총평
- 스택과 수동 백트래킹(`forks`, `route`, `went_points`, `walls`) 조합으로 미로 탐색을 구현함
- 도착점 도달 여부를 정확히 판단하며, 막다른 길을 벽으로 처리해 재탐색하는 로직이 동작함
- `where_to_go` 함수로 이동 후보를 필터링해 분리된 책임을 가짐

<br><br>

# 보완점
## 1. BFS/DFS 단순화 및 명확화
현재 수동으로 갈림길을 관리하는 대신, `collections.deque`를 이용한 BFS(또는 재귀 DFS)를 사용하면 한 번의 순차적 탐색으로 도착 가능 여부를 판단할 수 있습니다.
```python
from collections import deque

def exists_path(maze, start, end):
    N = len(maze)
    visited = [[False]*N for _ in range(N)]
    dq = deque([start])
    visited[start[0]][start[1]] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while dq:
        x, y = dq.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                dq.append((nx, ny))
    return False
```

## 2. 전역 상태 제거 및 입력 분리
- `walls`, `went_points` 같은 전역 변수를 제거하고, 함수 내부로 모든 상태를 캡슐화하세요.
- 입력 처리와 탐색 로직을 `solve()` 함수로 분리해 가독성과 재사용성을 높입니다.

## 3. 가독성을 위한 자료구조와 변수명 정리
- `arr`보다 `maze`나 `board` 같은 명확한 이름 사용
- 이동 방향 델타를 상수 `directions`로 정의해 코드 중복 제거


<br><br>

# 최종 코드 예시
```python
import sys
from collections import deque

def exists_path(maze, start, end):
    N = len(maze)
    visited = [[False]*N for _ in range(N)]
    dq = deque([start])
    visited[start[0]][start[1]] = True
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while dq:
        x, y = dq.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                dq.append((nx, ny))
    return False


def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T+1):
        N = int(input().strip())
        maze = [list(map(int, input().strip())) for _ in range(N)]
        start = end = None
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    start = (i, j)
                elif maze[i][j] == 3:
                    end = (i, j)
        result = 1 if exists_path(maze, start, end) else 0
        print(f"#{tc} {result}")

if __name__ == '__main__':
    solve()
```  