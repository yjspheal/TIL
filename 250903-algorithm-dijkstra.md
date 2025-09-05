- [1. 다익스트라(Dijkstra) 알고리즘이란?](#1-다익스트라dijkstra-알고리즘이란)
- [2. 알고리즘 동작 원리](#2-알고리즘-동작-원리)
- [3. 파이썬 구현 (우선순위 큐)](#3-파이썬-구현-우선순위-큐)
- [4. 특징 및 제약사항](#4-특징-및-제약사항)

---

## 1. 다익스트라(Dijkstra) 알고리즘이란?

- 그래프에서 `하나의 시작 정점(Single Source)`으로부터 다른 모든 정점까지의 `최단 경로(Shortest Path)`를 찾는 알고리즘
- 각 간선(edge)의 가중치(weight)는 `음수가 아니어야 한다`는 핵심적인 제약 조건을 가짐

## 2. 알고리즘 동작 원리

- `우선순위 큐(Priority Queue)`를 사용하는 방식이 효율적이며 일반적임 (Python의 `heapq` 모듈)

1.  **초기화**
    - 출발 노드까지의 거리는 0, 나머지 모든 노드까지의 거리는 무한(`inf`)으로 설정한 거리 테이블을 준비
    - 우선순위 큐에 `(거리, 노드)` 형태로 `(0, 시작 노드)`를 추가

2.  **반복**
    - 우선순위 큐가 비어있지 않은 동안 다음을 반복:
    - 큐에서 현재 시점의 최단 거리를 가진 노드를 꺼냄 (`heappop`)
    - 만약 이미 처리된 노드(더 짧은 경로가 발견된 노드)라면 무시
    - 현재 노드와 인접한 노드들을 순회하며, 현재 노드를 거쳐 가는 것이 더 짧은 경로인지 확인
    - 더 짧은 경로가 발견되면, 거리 테이블을 업데이트하고 해당 정보를 `(새로운 거리, 인접 노드)` 형태로 우선순위 큐에 추가 (`heappush`)

## 3. 파이썬 구현 (우선순위 큐)

```python
import heapq

def dijkstra(graph, start):
    # 1. 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)] # (거리, 노드)
    
    # 2. 반복
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 더 짧은 경로가 발견되었다면 무시
        if current_distance > distances[current_node]:
            continue
            
        # 현재 노드와 인접한 노드 확인
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로 발견 시 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# 예시 그래프 (인접 리스트 형태의 딕셔너리)
my_graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

shortest_paths = dijkstra(my_graph, 'A')
# 결과: {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
```

## 4. 특징 및 제약사항

- **그리디(Greedy) 알고리즘**: 매 순간 가장 비용이 적은 경로를 선택하여 최적해를 찾아감
- **시간 복잡도**: 우선순위 큐 사용 시 `**O(E log V)**` (E: 간선 수, V: 정점 수)
- **제약사항**: 간선의 가중치가 `**음수**`인 경우에는 사용할 수 없음
    - 음수 가중치가 있는 경우, 방문 처리된 노드까지의 최단 거리가 나중에 갱신될 수 있어 알고리즘의 기본 가정이 깨짐
    - 음수 사이클이 없는 음수 가중치 그래프는 `**벨만-포드(Bellman-Ford)**` 알고리즘을 사용해야 함
