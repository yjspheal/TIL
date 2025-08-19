

- [상속](#상속)
  - [필요한 이유](#필요한-이유)
- [클래스 상속](#클래스-상속)
- [메서드 오버라이딩](#메서드-오버라이딩)
  - [\[참고\] 오버로딩은 뭔가요?](#참고-오버로딩은-뭔가요)
- [다중 상속](#다중-상속)
- [다이아몬드 문제 (The Diamond Problem)](#다이아몬드-문제-the-diamond-problem)
  - [문제 상황](#문제-상황)
- [파이썬에서의 해결책: MRO (Method Resolution Order)](#파이썬에서의-해결책-mro-method-resolution-order)
  - [예시](#예시)
- [super() 함수](#super-함수)
  - [단일상속에서의 사용](#단일상속에서의-사용)
  - [다중 상속에서의 사용](#다중-상속에서의-사용)
  - [동작 설명](#동작-설명)
  - [`show_value()` 실행 흐름](#show_value-실행-흐름)
  - [`mro()`, `__mro__`로 확인 가능](#mro-__mro__로-확인-가능)
- [버그와 디버깅](#버그와-디버깅)
  - [버그](#버그)
  - [디버깅](#디버깅)
- [에러와 예외](#에러와-예외)
  - [문법 에러(SyntaxError)](#문법-에러syntaxerror)
  - [예외](#예외)
    - [내장 예외](#내장-예외)
  - [예외처리(Exception Handling)](#예외처리exception-handling)
  - [EAFP \& LBYL](#eafp--lbyl)
- [메서드 오버라이딩 vs 오버로딩](#메서드-오버라이딩-vs-오버로딩)
  - [내용](#내용)
    - [오버라이딩 (Method Overriding)](#오버라이딩-method-overriding)
    - [오버로딩 (Method Overloading)](#오버로딩-method-overloading)
- [메서드 오버라이딩 시 주의할 점](#메서드-오버라이딩-시-주의할-점)
  - [내용](#내용-1)
  - [예시](#예시-1)
  - [결론](#결론)
- [클래스 메서드가 필요한 이유](#클래스-메서드가-필요한-이유)
  - [내용](#내용-2)
  - [예시 코드](#예시-코드)
  - [요약](#요약)

---

## 상속

- 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)이 물려받는 것
- 부모와 자식 간의 상하 관계가 형성됨
- 부모는 본인의 속성과 메서드를 자식에게 넘겨줌 → 이를 상속이라고 함

### 필요한 이유

- 코드 재사용
- 계층 구조(더 구체적인 클래스를 만들 수 있음)
- 유지보수 용이(기존 클래스 수정 시 영향이 적음)

---

## 클래스 상속

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
```

- 아 다 좋은데 저거 self 다 써야되나?
  - No. `super()`라는 함수가 존재한다! 뒤에 나옴

---

## 메서드 오버라이딩

- 부모 클래스에 있는 메서드를, 같은 이름과 같은 파라미터 구조로 재정의 하는 것
    - ex) 부모 클래스에 talk(self)가 있는데 자식에 또 talk(self)로 하는 것.
    - 부모 클래스의 기능을 유지하면서도, 일부 동작을 맞춤형으로 하고자 할 때 사용
- 즉, 덮어쓰기(override)

Q. 근데 왜 같은 파라미터 구조를 해야돼요?

A. 파라미터 구조를 다르게 오버라이딩하면, 객체 지향 프로그래밍의 핵심 개념인 다형성(Polymorphism)을 위반하여 예기치 않은 오류를 유발합니다.

---

### [참고] 오버로딩은 뭔가요?

- ‘하나’의 클래스 안에서, 파라미터가 다른 동일한 이름의 여러 메서드를 정의하는 것
- 파이썬에선 지원 x.

---

## 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있음
- 모든 부모의 요소 사용 가능
    - 중복 속성/메서드가 있는 경우, 순서에 의해 결정됨(앞에 게 우선)

- 앞에 상속된 것이 우선
  - `class Baby(Dad, Mother)` 이라면, Dad가 우선

- 이를 diamond problem이라고 함

---

## 다이아몬드 문제 (The Diamond Problem)

- 두 클래스 B와 C가 A로부터 상속되고, D가 B와 C를 모두 상속할 때 발생하는 모호성 문제

### 문제 상황

- B, C 모두 A에 있는 동일한 메서드를 재정의하지 않은 경우
- D는 그 메서드를 B로부터 상속받아야 하는가? C로부터 상속받아야 하는가?

즉, 상속 계층 구조가 다이아몬드 모양이 되어 우선순위가 모호해짐

```
    A
   / \
  B   C
   \ /
    D
```

---

## 파이썬에서의 해결책: MRO (Method Resolution Order)

- MRO는 파이썬이 메서드를 찾는 우선순위 규칙을 정의한 것
- 좌→우, 깊이 우선(DFS) 방식으로 탐색, 중복 클래스는 한 번만 확인
- 파이썬 내부 알고리즘(C3 선형화)에 따라 결정됨

### 예시
```python
class D(B, C):
    pass
```
- 속성이 D에 없으면 → B → C → A 순으로 검색

---

## super() 함수
- MRO에 따라 현재 클래스의 부모(상위)클래스의 메서드나 속성에 접근할 수 있게 해주는 내장 함수
- 단일상속에선 그냥 그렇지만, 다중 상속에선 매우 중요!
<br>

### 단일상속에서의 사용
- `부모클래스이름.__init__~~`로 직접 해도 되지만, super()를 쓰면 나중에 클래스 이름 바뀌어도 코드 유지가 쉬움
<br>

### 다중 상속에서의 사용

```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        self.value_c = 'Child'
    def show_value(self):
        super().show_value()
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()

print(child.value_c)
print(child.value_a)
```

### 동작 설명

1. Child는 ParentA, ParentB를 순서대로 상속
2. `child = Child()` 실행 시 Child의 __init__에서 `super().__init__()` 호출
3. MRO에 따라 Child → ParentA → ParentB 순서로 탐색 → `ParentA.__init__()` 호출
4. 결과적으로 value_a만 초기화됨 (`ParentB.__init__()`은 자동 호출 X)

- `ParentA.__init__()` 내에서 `super().__init__()` 호출 시 `ParentB.__init__()`까지 호출됨

### `show_value()` 실행 흐름

- `child.show_value()` 호출 시 `Child.show_value()` → `super().show_value()` → `ParentA.show_value()` 호출
- `ParentB.show_value()`는 호출되지 않음

### `mro()`, `__mro__`로 확인 가능
```python
print(D.mro())
print(D.__mro__)
```
---

## 버그와 디버깅

### 버그

- 소프트웨어에서 발생하는 오류/결함, 예상 동작과 실제 동작의 불일치

### 디버깅

- 버그를 찾아 수정하는 과정
- 단계별 코드 실행, 로그 출력, Python tutor, IDE, 눈으로 찾기 등

---

## 에러와 예외

### 문법 에러(SyntaxError)

- 실행 자체가 안 되는 에러(구문 문제)

### 예외

- 프로그램 실행 중에 감지되는 에러

#### 내장 예외

- ZeroDivisionError 등, 상황별 내장 예외 발생

### 예외처리(Exception Handling)

- try - except 문으로 적절히 처리 가능
- else, finally 블록으로 추가 처리도 가능

### EAFP & LBYL

- EAFP: try - except로 우선 실행, 실패시 처리
- LBYL: if - else로 사전 검사

---

## 메서드 오버라이딩 vs 오버로딩

### 내용

#### 오버라이딩 (Method Overriding)
- 상속 관계에서 부모 클래스의 메서드를 같은 이름, 같은 파라미터로 재정의
- Python: 공식적으로 지원

#### 오버로딩 (Method Overloading)
- 같은 클래스 내에서 이름은 같고, 파라미터가 다른 메서드를 여러 개 정의 (파이썬 공식 미지원)

| 구분       | 오버라이딩                   | 오버로딩                         |
|------------|------------------------------|----------------------------------|
| 목적       | 부모 메서드의 동작 수정      | 같은 이름의 메서드를 다양하게 사용 |
| 범위       | 상속(다른 클래스)            | 클래스 내부(같은 클래스)         |
| Python     | 지원                         | 미지원                          |

---

## 메서드 오버라이딩 시 주의할 점

### 내용

- 오버라이딩할 때는 이름과 파라미터 구조를 반드시 부모와 동일하게!
- 구조가 달라도 파이썬은 에러를 내지 않으나, 다형성이 깨져 예기치 않은 에러 유발 가능

### 예시
```python
class Animal:
    def eat(self):
        print("Animal이 먹는 중")

class Dog(Animal):
    def eat(self, food):  # 잘못된 오버라이딩
        print(f"Dog가 {food}를 먹는 중")

def feed_animal(animal):
    animal.eat()

dog = Dog()
feed_animal(dog)  # TypeError 발생
```

- 부모는 eat(self), 자식이 eat(self, food)로 바꾸면 부모 타입으로 객체를 쓸 때 TypeError 발생

### 결론

- 오버라이딩은 동작만 다르게, 시그니처(이름/파라미터)는 동일하게!
- 올바른 오버라이딩만이 다형성을 안전하게 보장

---

## 클래스 메서드가 필요한 이유

### 내용

클래스 메서드는
- 인스턴스 생성 없이도 클래스 상태(속성) 관리
- 상속 관계에서 부모/자식 클래스가 각자 클래스를 기준으로 동작 가능

### 예시 코드

```python
class Animal:
    total_count = 0
    def __init__(self, name):
        self.name = name
        Animal.total_count += 1
    @classmethod
    def get_total_count(cls):
        return f'전체 동물 수: {cls.total_count}'

class Dog(Animal):
    dog_count = 0
    def __init__(self, name, breed):
        super().__init__(name)
        Dog.dog_count += 1
    @classmethod
    def get_dog_info(cls):
        return f'{cls.get_total_count()}, 강아지 수: {cls.dog_count}'

dog1 = Dog("멍멍이", "진돗개")
dog2 = Dog("초코", "말티즈")
print(Dog.get_dog_info())  # 전체 동물 수: 2, 강아지 수: 2
```

### 요약

- 클래스 메서드는 코드 중복 줄이기, 클래스 단위 데이터 관리, 상속 구조에서의 효율성/유지보수성↑
- cls는 호출한 클래스를 정확하게 가리켜줌

---
