# Java Day 3 - 문자열, 배열, ArrayList

## 1. String

Java에서 문자열은 `String`을 사용한다.

```java
String name = "YJ";
System.out.println(name);
```

### 문자열 비교

문자열의 **내용이 같은지 비교**할 때는 `equals()`를 사용한다.

```java
String a = "hello";
String b = "hello";

System.out.println(a.equals(b)); // true
```

`==`는 문자열 내용 비교에 사용하는 것이 아니라 참조 비교와 관련되므로, 문자열 비교에서는 `equals()`를 사용하는 것이 중요하다.

### 자주 사용하는 String 메서드

```text
length()          → 문자열 길이
charAt(i)         → i번째 문자
substring(a, b)   → a부터 b 직전까지
toUpperCase()     → 대문자로 변환
toLowerCase()     → 소문자로 변환
equals()          → 문자열 내용 비교
```

예시:

```java
String s = "Hello";

System.out.println(s.length());        // 5
System.out.println(s.charAt(1));       // e
System.out.println(s.substring(1, 4)); // ell
System.out.println(s.toUpperCase());   // HELLO
System.out.println(s.toLowerCase());   // hello
```

`substring(시작, 끝)`에서 **끝 인덱스는 포함하지 않는다.**

---

## 2. 배열

Java 배열은 C의 배열과 비슷하게 인덱스를 0부터 사용한다.

```java
int[] arr = {10, 20, 30};

System.out.println(arr[0]);     // 10
System.out.println(arr.length); // 3
```

반복문으로 순회할 수 있다.

```java
for (int i = 0; i < arr.length; i++) {
    System.out.print(arr[i] + " ");
}
```

출력:

```text
10 20 30
```

### 배열과 문자열의 length 차이

```text
문자열 → s.length()
배열   → arr.length
```

문자열은 메서드이므로 `()`, 배열은 필드이므로 `()`가 없다.

---

## 3. ArrayList

`ArrayList`는 여러 값을 저장할 수 있는 컬렉션이며, 배열과 달리 크기가 자동으로 늘어나거나 줄어들 수 있다.

```java
import java.util.ArrayList;

ArrayList<String> list = new ArrayList<>();

list.add("A");
list.add("B");

System.out.println(list.get(0)); // A
System.out.println(list.size()); // 2
```

### 주요 메서드

```text
add()     → 값 추가
get(i)    → i번째 값 가져오기
remove()  → 값 또는 인덱스 삭제
size()    → 현재 원소 개수
```

### remove 예시

```java
ArrayList<String> list = new ArrayList<>();

list.add("A");
list.add("B");
list.add("C");

list.remove(1);

System.out.println(list.get(1));
```

`1`번 인덱스인 `B`가 삭제되므로 리스트는

```text
[A, C]
```

가 되고, `list.get(1)`은 `C`를 반환한다.

---

## 4. ArrayList 반복문

```java
ArrayList<Integer> list = new ArrayList<>();

list.add(10);
list.add(20);
list.add(30);

for (int i = 0; i < list.size(); i++) {
    System.out.print(list.get(i) + " ");
}
```

출력:

```text
10 20 30
```

`list.size()`는 현재 원소의 개수이고, `list.get(i)`로 해당 위치의 값을 가져온다.

---

## 5. 오늘 헷갈렸던 부분

### 문자열 비교

```java
a.equals(b)
```

→ 두 문자열의 **내용이 같은지** 비교

### substring

```java
s.substring(1, 4)
```

→ 1번부터 4번 **직전**까지

### length / size

```text
String     → length()
배열       → length
ArrayList  → size()
```

---

## 6. 오늘의 핵심 암기

```text
String
→ length(), charAt(), substring(), toUpperCase(), toLowerCase(), equals()

배열
→ arr.length

ArrayList
→ add(), get(), remove(), size()

문자열 내용 비교
→ equals()
```

## 7. 오늘의 학습 정리

오늘은 시간이 부족해서 Java의 문자열, 배열, 컬렉션 중 `ArrayList`의 핵심 기능을 빠르게 복습했다.

특히 시험에서 코드 실행 문제로 자주 나올 수 있는

- 문자열 인덱스
- `substring()`의 끝 인덱스 미포함
- 배열의 `length`
- `ArrayList`의 `size()`
- `add()`, `get()`, `remove()`
- 문자열 비교 시 `equals()`

를 중심으로 공부했다.

컬렉션의 나머지 내용은 이후 기출 문제를 풀면서 필요한 부분을 추가 학습한다.
