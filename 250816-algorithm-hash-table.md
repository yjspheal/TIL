- [해시 테이블 (Hash Table)](#해시-테이블-hash-table)
  - [개념](#개념)
  - [주요 구성 요소](#주요-구성-요소)
  - [해시 함수 (Hash Function)](#해시-함수-hash-function)
  - [해시 충돌 (Hash Collision)](#해시-충돌-hash-collision)
    - [충돌 해결 방법](#충돌-해결-방법)
  - [성능](#성능)
  - [Python의 딕셔너리 (dict)](#python의-딕셔너리-dict)
  - [Python 예시 (간단한 구현)](#python-예시-간단한-구현)

---

## 해시 테이블 (Hash Table)

### 개념
- 키(Key)를 값(Value)에 매핑하는 데 사용되는 자료구조.
- 내부적으로 배열(버킷 또는 슬롯)을 사용하여 데이터를 저장하며, **해시 함수(Hash Function)**를 통해 키를 배열의 인덱스로 변환하여 데이터를 빠르게 찾을 수 있도록 한다.
- 데이터의 삽입, 삭제, 검색이 평균적으로 `O(1)`의 시간 복잡도를 가진다.

### 주요 구성 요소
- **키 (Key)**: 데이터를 식별하는 고유한 값.
- **값 (Value)**: 키에 연결된 실제 데이터.
- **해시 함수 (Hash Function)**: 키를 배열의 유효한 인덱스(해시 값)로 변환하는 함수.
- **해시 값 (Hash Value) / 인덱스**: 해시 함수가 반환하는 배열의 위치.
- **버킷 (Bucket) / 슬롯 (Slot)**: 해시 테이블 내부의 배열 요소. 실제 데이터가 저장되는 공간.

### 해시 함수 (Hash Function)
- 임의의 크기를 가진 데이터를 고정된 크기의 해시 값으로 매핑하는 함수.
- 좋은 해시 함수는 충돌(서로 다른 키가 같은 해시 값을 가지는 현상)을 최소화하고, 해시 값을 고르게 분포시켜야 한다.

### 해시 충돌 (Hash Collision)
- 서로 다른 두 개 이상의 키가 동일한 해시 값을 가지게 되어 같은 버킷에 저장되려는 현상.
- 해시 테이블의 성능에 직접적인 영향을 미치므로, 충돌을 효율적으로 해결하는 것이 중요하다.

#### 충돌 해결 방법
1.  **개별 체이닝 (Separate Chaining)**:
    - 각 버킷이 연결 리스트(또는 다른 자료구조)를 사용하여 해당 버킷으로 해시된 모든 키-값 쌍을 저장한다.
    - 충돌이 발생하면 해당 버킷의 연결 리스트에 새 요소를 추가한다.
2.  **개방 주소법 (Open Addressing)**:
    - 충돌이 발생하면, 해시 테이블 내의 다른 빈 슬롯을 찾아 데이터를 저장한다.
    - **선형 탐사 (Linear Probing)**: 충돌 시 다음 빈 슬롯을 순차적으로 탐색.
    - **제곱 탐사 (Quadratic Probing)**: 충돌 시 제곱수를 더해 탐사 간격을 늘림.
    - **이중 해싱 (Double Hashing)**: 두 번째 해시 함수를 사용하여 탐사 간격을 결정.

### 성능
- **평균 시간 복잡도**: 삽입, 삭제, 검색 모두 `O(1)`.
- **최악 시간 복잡도**: 모든 키가 하나의 버킷으로 해시되는 경우 `O(N)` (N은 요소의 개수).
- 해시 함수의 성능과 충돌 해결 전략에 따라 실제 성능이 달라진다.

### Python의 딕셔너리 (dict)
- Python의 내장 딕셔너리 타입은 해시 테이블로 구현되어 있다.
- 따라서 키-값 쌍의 저장, 검색, 삭제가 매우 효율적이다.

### Python 예시 (간단한 구현)
- 개별 체이닝 방식을 사용한 매우 간단한 해시 테이블 구현 예시.

```python
class SimpleHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)] # 각 버킷은 리스트

    def _hash(self, key):
        # 간단한 해시 함수 (키의 문자열 합을 용량으로 나눈 나머지)
        return sum(ord(char) for char in str(key)) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        # 이미 존재하는 키인지 확인 후 업데이트 또는 추가
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value) # 값 업데이트
                return
        self.table[index].append((key, value)) # 새 키-값 쌍 추가

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None # 키를 찾지 못함

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True # 삭제 성공
        return False # 키를 찾지 못함

# 해시 테이블 사용 예시
ht = SimpleHashTable(capacity=10)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)
ht.insert("apple", 15) # 값 업데이트

print(f"apple의 값: {ht.search("apple")}")   # 15
print(f"banana의 값: {ht.search("banana")}") # 20
print(f"grape의 값: {ht.search("grape")}")   # None

ht.delete("banana")
print(f"banana 삭제 후: {ht.search("banana")}") # None
print(f"cherry 삭제 시도: {ht.delete("cherry")}") # True
```
