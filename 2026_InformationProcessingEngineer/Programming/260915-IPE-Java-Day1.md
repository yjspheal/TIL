
- [**변수와 자료형**](#변수와-자료형)
- [**배열**](#배열)
- [**클래스와 객체**](#클래스와-객체)
- [**메서드**](#메서드)
- [**생성자**](#생성자)
- [**상속**](#상속)
- [**오버라이딩**](#오버라이딩)
- [**다형성**](#다형성)
- [**super**](#super)
- [**this**](#this)
- [**오늘 배운 내용**](#오늘-배운-내용)


# **변수와 자료형**

Java에서는 변수를 선언할 때 자료형을 명시한다.

```java
int a = 10;
String name = "Kim";
boolean flag = true;
```

```text
int
→ 정수형

String
→ 문자열

boolean
→ 논리형
```

정수형 변수끼리 나눗셈을 하면 정수 나눗셈이 이루어진다.

```java
int a = 10;
int b = 3;

System.out.println(a / b);
```

→ `3`

실수형이 포함되면 실수 나눗셈이 된다.

```java
System.out.println(10.0 / 3);
```

→ `3.333...`


# **배열**

Java 배열은 0부터 인덱스가 시작한다.

```java
int[] arr = {10, 20, 30, 40};

System.out.println(arr[1]);
```

→ `20`

배열의 길이는 `length`로 확인한다.

```java
arr.length
```

→ `4`


# **클래스와 객체**

클래스는 객체가 가지는 필드와 메서드를 정의한다.

```java
class Student {
    int age;

    void printAge() {
        System.out.println(age);
    }
}
```

객체는 `new`를 사용하여 생성한다.

```java
Student s = new Student();
```

```text
Student
→ 참조 타입

s
→ 참조 변수

new Student()
→ Student 객체 생성
```

객체의 필드와 메서드는 `.`으로 접근한다.

```java
s.age = 20;
s.printAge();
```


# **메서드**

객체의 동작을 정의하는 부분이다.

```java
class Student {
    int age = 20;

    void addAge(int n) {
        age += n;
    }
}
```

```java
Student s = new Student();

s.addAge(5);
```

→ `age`가 `20`에서 `25`로 변경된다.

```text
5
→ 인자(argument)

n
→ 매개변수(parameter)
```


# **생성자**

생성자는 객체가 생성될 때 호출되는 특별한 메서드 형태이다.

특징:

```text
클래스 이름과 동일
반환형 없음
객체 생성 시 호출
```

```java
class Student {
    int age;

    Student(int age) {
        this.age = age;
    }
}
```

```java
Student s = new Student(25);
```

→ `age`가 `25`인 Student 객체 생성

생성자를 사용하면 객체 생성과 동시에 필요한 초기값을 설정할 수 있다.


# **상속**

`extends`를 사용하여 다른 클래스의 필드와 메서드를 상속받을 수 있다.

```java
class Parent {
    int x = 10;
}

class Child extends Parent {
    int y = 20;
}
```

```java
Child c = new Child();

System.out.println(c.x);
System.out.println(c.y);
```

→ 부모에게서 상속받은 `x`와 자식이 가진 `y`를 모두 사용할 수 있다.


# **오버라이딩**

자식 클래스에서 부모 클래스의 메서드를 재정의하는 것을 오버라이딩이라고 한다.

```java
class Parent {
    void print() {
        System.out.println("Parent");
    }
}

class Child extends Parent {
    @Override
    void print() {
        System.out.println("Child");
    }
}
```

```java
Child c = new Child();
c.print();
```

→ `Child` 출력


# **다형성**

부모 타입의 참조 변수로 자식 객체를 참조할 수 있다.

```java
Parent p = new Child();
```

이 경우:

```text
변수의 타입 → Parent
실제 객체   → Child
```

오버라이딩된 메서드를 호출하면 실제 객체인 `Child`의 메서드가 실행된다.

```java
p.print();
```

→ `Child`


# **super**

`super`는 부모 클래스의 멤버나 생성자를 명시적으로 참조할 때 사용한다.

```java
class Parent {
    int age = 50;
}

class Child extends Parent {
    int age = 20;

    void printAge() {
        System.out.println(age);
        System.out.println(super.age);
    }
}
```

결과:

```text
20
50
```

```text
age
→ 현재 클래스의 age

super.age
→ 부모 클래스의 age
```

부모 생성자를 호출할 때도 사용할 수 있다.

```java
super(10);
```

→ 부모 클래스의 생성자에 `10` 전달

객체 생성 시에는 부모 생성자가 먼저 실행된 후 자식 생성자가 실행된다.


# **this**

`this`는 현재 객체를 가리킨다.

```java
class Student {
    int age;

    Student(int age) {
        this.age = age;
    }
}
```

```text
this.age
→ 현재 객체의 필드

age
→ 생성자의 매개변수
```

따라서:

```java
Student s = new Student(20);
```

→ 객체의 `age`에 `20`이 저장된다.

# **오늘 배운 내용**

```text
int / String / boolean
→ 기본적인 자료형

배열
→ 0부터 시작
→ length로 길이 확인

class
→ 클래스 정의

new
→ 객체 생성

메서드
→ 객체의 동작

생성자
→ 객체 생성 시 호출
→ 클래스 이름과 동일
→ 반환형 없음

extends
→ 상속

@Override
→ 부모 메서드 재정의

Parent p = new Child()
→ 변수 타입은 Parent
→ 실제 객체는 Child
→ 오버라이딩된 메서드는 Child가 실행

super
→ 부모 클래스

this
→ 현재 객체
```