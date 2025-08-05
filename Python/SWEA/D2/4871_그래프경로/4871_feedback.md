- [총평](#총평)
- [보완점](#보완점)
  - [1. 전역 변수(`answer`) 제거 및 함수 반환 방식 변경](#1-전역-변수answer-제거-및-함수-반환-방식-변경)
  - [2. BFS(너비 우선 탐색) 사용으로 재귀 깊이 제한 회피](#2-bfs너비-우선-탐색-사용으로-재귀-깊이-제한-회피)
- [최종 코드 예시](#최종-코드-예시)


<br>

# 총평
- 인접 리스트(adjacency list)를 사용해 그래프를 표현한 점이 적절함
- DFS(깊이 우선 탐색)를 통해 출발 노드에서 목표 노드로의 경로 존재 여부를 정확히 판단함
- 방문 체크(`visited`)로 사이클이나 중복 탐색을 방지하여 무한 재귀를 예방함

<br>

# 보완점
## 1. 전역 변수(`answer`) 제거 및 함수 반환 방식 변경
현재 `answer`를 전역 변수로 선언하고 DFS 내에서 갱신하는 구조는 코드 가독성을 떨어뜨립니다. 대신 DFS 함수가 목표를 찾으면 `True`를 반환하고, 이를 호출부에서 처리하도록 변경하세요.
```python
# 반환값으로 탐색 성공 여부를 전달
def dfs(node):
    if node == G:
        return True
    visited[node] = True
    for nxt in adj[node]:
        if not visited[nxt] and dfs(nxt):
            return True
    return False
```
<br>

## 2. BFS(너비 우선 탐색) 사용으로 재귀 깊이 제한 회피
경로 존재 여부만 확인할 경우 BFS를 사용하면 재귀 호출 깊이에 대한 제한 없이 안정적으로 동작합니다.
```python
from collections import deque

def exists_path(adj, S, G):
    q = deque([S])
    visited[S] = True
    while q:
        u = q.popleft()
        if u == G:
            return True
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return False
```
<br>
<br>

# 최종 코드 예시
```python
import sys
from collections import deque

input = sys.stdin.readline

def exists_path(adj, S, G):
    visited = [False] * len(adj)
    q = deque([S])
    visited[S] = True
    while q:
        u = q.popleft()
        if u == G:
            return True
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return False


def solve():
    T = int(input().strip())
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        S, G = map(int, input().split())
        result = 1 if exists_path(adj, S, G) else 0
        print(f"#{tc} {result}")

if __name__ == '__main__':
    solve()
```  