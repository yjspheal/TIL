# Java Day 2 - 접근 제어자, abstract, interface, 예외 처리

## 1. 접근 제어자

클래스의 필드나 메서드에 **어디에서 접근할 수 있는지**를 정하는 키워드이다.

| 접근 제어자 | 접근 범위 |
|---|---|
| `public` | 어디서든 접근 가능 |
| `protected` | 같은 클래스, 같은 패키지, 상속 관계에서 접근 가능 |
| `default` | 같은 패키지에서 접근 가능 |
| `private` | 같은 클래스에서만 접근 가능 |

### private과 getter/setter

`private` 필드는 클래스 외부에서 직접 접근할 수 없다.

```java
class Student {
    private int age;

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }
}
```

외부에서는 다음처럼 사용한다.

```java
Student s = new Student();

s.setAge(25);
System.out.println(s.getAge());
```

`setAge()`는 생성자가 아니라 **setter 메서드**이다.

- setter: 값을 설정
- getter: 값을 조회
- 생성자: 클래스와 같은 이름을 가지며 객체 생성 시 호출

---

## 2. abstract

### 추상 클래스

추상 클래스는 **공통적인 틀을 만들어 놓는 클래스**이다.

```java
abstract class Animal {
    abstract void sound();
}
```

위 코드에서

- `Animal` → 추상 클래스
- `sound()` → 추상 메서드

### 추상 메서드

추상 메서드는 **선언만 있고 구현 내용이 없는 메서드**이다.

```java
abstract void sound();
```

자식 클래스에서 실제 내용을 구현한다.

```java
class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("멍멍");
    }
}
```

추상 클래스는 직접 객체를 생성할 수 없다.

```java
Animal a = new Animal();   // 오류
```

하지만 자식 객체를 참조하는 것은 가능하다.

```java
Animal a = new Dog();
a.sound();   // 멍멍
```

여기서는 변수의 타입은 `Animal`이지만 실제 객체는 `Dog`이다.

따라서 `sound()`를 호출하면 `Dog`에서 구현한 메서드가 실행된다.

---

## 3. interface

인터페이스는 **특정 기능을 반드시 구현해야 한다는 규칙을 정하는 것**으로 이해했다.

```java
interface Flyable {
    void fly();
}
```

이것은 `Flyable`을 구현하는 클래스는 `fly()` 기능을 가져야 한다는 의미이다.

```java
class Airplane implements Flyable {
    @Override
    public void fly() {
        System.out.println("비행기가 날아갑니다.");
    }
}
```

사용:

```java
Airplane a = new Airplane();
a.fly();
```

출력:

```text
비행기가 날아갑니다.
```

### extends와 implements

```text
extends
→ 상속

implements
→ 인터페이스 구현
```

### abstract와 interface의 현재 이해

```text
abstract class
→ 공통적인 틀을 만들어 둠

interface
→ 반드시 구현해야 할 기능의 규칙을 정함
```

인터페이스 자체가 자동으로 기능을 실행하는 것은 아니다.

예를 들어

```java
Animal a1 = new Dog();
```

만 작성한다고 `멍멍`이 자동으로 출력되는 것은 아니다.

```java
a1.sound();
```

처럼 메서드를 호출해야 실제 구현된 메서드가 실행된다.

---

## 4. 예외 처리

프로그램 실행 중 발생하는 예상치 못한 문제를 예외(Exception)라고 한다.

예:

```java
int a = 10;
int b = 0;

System.out.println(a / b);
```

0으로 나누기 때문에 `ArithmeticException`이 발생한다.

### try-catch

예외가 발생할 수 있는 코드를 `try`에 작성하고, 예외가 발생했을 때의 처리를 `catch`에 작성한다.

```java
try {
    int x = 10 / 0;
    System.out.println(x);
} catch (ArithmeticException e) {
    System.out.println("오류 발생");
}
```

출력:

```text
오류 발생
```

예외가 발생한 이후 `try` 내부의 나머지 코드는 실행되지 않고 `catch`로 이동한다.

---

## 5. finally

`finally`는 예외 발생 여부와 관계없이 마지막에 실행된다.

```java
try {
    System.out.println("A");
    int x = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("B");
} finally {
    System.out.println("C");
}
```

출력:

```text
A
B
C
```

정리:

```text
try
→ 실행할 코드

catch
→ 예외가 발생했을 때 처리할 코드

finally
→ 마지막에 실행할 코드
```

---

## 6. throw와 throws

이름이 비슷하지만 역할이 다르다.

### throw

**실제로 예외를 발생시킨다.**

```java
throw new Exception();
```

Python의 `raise`와 비슷한 개념이다.

```python
raise Exception()
```

### throws

**해당 메서드에서 예외가 발생할 수 있다고 선언한다.**

```java
void test() throws Exception {
    // 예외가 발생할 수 있는 코드
}
```

정리:

```text
throw
→ 예외를 실제로 발생시킴

throws
→ 예외 발생 가능성을 선언함
```

---

## 7. 오늘 헷갈렸던 부분

### setAge는 생성자가 아니다

```java
public void setAge(int age) {
    this.age = age;
}
```

`setAge()`는 일반 메서드이며 setter이다.

생성자는 클래스와 같은 이름을 가진다.

```java
class Student {
    Student(int age) {
        this.age = age;
    }
}
```

### protected

`protected`는 단순히 같은 패키지뿐 아니라 **상속 관계에서도 접근할 수 있다.**

### interface

인터페이스를 구현했다고 해서 메서드가 자동으로 실행되는 것은 아니다.

```java
Animal a = new Dog();
```

객체를 만든 것뿐이고,

```java
a.sound();
```

처럼 메서드를 호출해야 실행된다.

---

## 8. 오늘의 핵심 암기

```text
public    → 어디서든
protected → 같은 패키지 + 상속
default   → 같은 패키지
private   → 같은 클래스

abstract  → 공통 틀
interface → 구현해야 할 기능의 규칙

extends   → 상속
implements → 인터페이스 구현

try       → 예외가 발생할 수 있는 코드
catch     → 예외 처리
finally   → 마지막에 실행

throw     → 예외를 발생시킴
throws    → 예외 발생 가능성을 선언
```

## 9. 느낀 점

오늘은 Java에서 객체지향 개념과 예외 처리의 연결을 공부했다.

특히 `abstract`와 `interface`의 차이를 처음에는 명확하게 이해하지 못했지만,

- `abstract`는 공통적인 틀
- `interface`는 반드시 구현해야 할 기능의 규칙

으로 정리하면서 개념을 잡을 수 있었다.

또한 `throw`는 Python의 `raise`와 비슷하다는 점을 연결해서 이해하니 기억하기 쉬웠다.
