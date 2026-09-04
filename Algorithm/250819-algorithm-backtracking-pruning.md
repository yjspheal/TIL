- [백트래킹 (Backtracking)](#백트래킹-backtracking)
  - [개념](#개념)
  - [동작 방식 (재귀적 구현)](#동작-방식-재귀적-구현)
- [부분집합 계산 (Subset Generation)](#부분집합-계산-subset-generation)
  - [백트래킹을 이용한 부분집합 생성](#백트래킹을-이용한-부분집합-생성)
  - [Python 예시](#python-예시)
- [가지치기 (Pruning)](#가지치기-pruning)
  - [개념](#개념-1)
  - [가지치기 적용 예시 (부분집합의 합)](#가지치기-적용-예시-부분집합의-합)

---

## 백트래킹 (Backtracking)

### 개념
- 모든 가능한 경우의 수를 탐색하는 **상태 공간 트리(State-Space Tree)**를 만들고, 해가 될 가능성이 없는 경로(branch)는 더 이상 탐색하지 않고 이전으로 돌아가 다른 경로를 찾는 알고리즘.
- 깊이 우선 탐색(DFS)을 기반으로 하며, 재귀 함수를 사용하여 구현하는 것이 일반적이다. (재귀 호출이 시스템 스택을 사용)
- 대표적인 문제: N-Queens, 미로 찾기, 부분집합 생성 등.

### 동작 방식 (재귀적 구현)
1.  **상태 공간 트리**를 정의한다. (문제 해결 과정의 각 단계를 노드로 표현)
2.  **깊이 우선 탐색**으로 트리를 탐색한다.
3.  현재 노드가 유망한지(promising) 확인한다. 즉, 현재 상태가 해답으로 이어질 가능성이 있는지 검사한다.
4.  **유망하지 않다면(non-promising)**, 부모 노드로 되돌아가(backtrack) 다른 자식 노드를 탐색한다. 이 과정을 **가지치기(Pruning)**라고 한다.
5.  종료 조건(leaf node)에 도달하면, 해를 찾았거나 더 이상 탐색할 곳이 없는 것이다.

---

## 부분집합 계산 (Subset Generation)

### 백트래킹을 이용한 부분집합 생성
- 주어진 집합의 각 원소에 대해 "부분집합에 포함시킬 것인가?" 또는 "포함시키지 않을 것인가?"의 두 가지 선택을 재귀적으로 반복하여 모든 부분집합을 생성할 수 있다.

### Python 예시
```python
def generate_subsets(arr):
    subsets = []
    current_subset = []

    def backtrack(index):
        # 현재까지 만들어진 부분집합을 결과에 추가
        subsets.append(list(current_subset))

        # 현재 인덱스부터 배열 끝까지 탐색
        for i in range(index, len(arr)):
            # 1. 원소를 선택 (포함시킴)
            current_subset.append(arr[i])
            # 2. 다음 원소로 재귀 호출
            backtrack(i + 1)
            # 3. 선택을 취소하고 되돌아감 (백트래킹)
            current_subset.pop()

    backtrack(0)
    return subsets

arr = [1, 2, 3]
all_subsets = generate_subsets(arr)
print(f"{arr}의 모든 부분집합: {all_subsets}")
# 결과: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

---

## 가지치기 (Pruning)

### 개념
- 백트래킹 알고리즘의 효율성을 높이기 위한 최적화 기법.
- **불필요한 탐색을 중단**하는 것. 즉, 현재 경로가 명백히 해답으로 이어질 수 없는 경우, 더 이상 깊이 들어가지 않고 탐색을 포기한다.
- 문제의 제약 조건을 활용하여 유망하지 않은 노드를 미리 차단한다.

### 가지치기 적용 예시 (부분집합의 합)
- **문제**: 주어진 배열의 부분집합 중, 원소의 합이 10이 되는 경우를 찾아라.
- **가지치기 조건**: 만약 현재까지 만든 부분집합의 합이 이미 10을 초과했다면, 더 이상 다른 원소를 추가해도 합이 10이 될 수 없다. 따라서 이 경로는 더 탐색할 필요가 없다.

```python
def find_subsets_with_sum(arr, target_sum):
    result = []
    current_subset = []

    def backtrack(index, current_sum):
        # 가지치기: 현재 합이 목표 합을 초과하면 더 이상 탐색하지 않음
        if current_sum > target_sum:
            return

        # 목표 합에 도달하면 결과에 추가
        if current_sum == target_sum:
            result.append(list(current_subset))
            return
        
        # 베이스 케이스: 모든 원소를 다 확인했으면 종료
        if index == len(arr):
            return

        # 현재 원소를 포함하는 경우
        current_subset.append(arr[index])
        backtrack(index + 1, current_sum + arr[index])
        current_subset.pop() # 백트래킹

        # 현재 원소를 포함하지 않는 경우
        backtrack(index + 1, current_sum)

    backtrack(0, 0)
    return result

arr = [1, 2, 3, 4, 5, 6, 7]
target = 10
subsets = find_subsets_with_sum(arr, target)
print(f"원소의 합이 {target}이 되는 부분집합: {subsets}")
# 결과: [[1, 2, 3, 4], [1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5], [3, 7], [4, 6]]
```
