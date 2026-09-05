- [SQL 기본 문법](#sql-기본-문법)
  - [SELECT, FROM](#select-from)
    - [모든 컬럼 조회](#모든-컬럼-조회)
    - [특정 컬럼 조회](#특정-컬럼-조회)
  - [WHERE](#where)
    - [비교 연산자](#비교-연산자)
  - [AND, OR](#and-or)
    - [AND](#and)
    - [OR](#or)
  - [BETWEEN](#between)
  - [IN](#in)
  - [LIKE](#like)
    - [여러 글자 와일드카드](#여러-글자-와일드카드)
    - [한 글자 와일드카드](#한-글자-와일드카드)
    - [두 와일드카드 비교](#두-와일드카드-비교)
  - [ORDER BY](#order-by)
    - [정렬 방향](#정렬-방향)
- [궁금증](#궁금증)
  - [문자열에 작은따옴표를 사용하는 이유](#문자열에-작은따옴표를-사용하는-이유)
- [실수한 부분](#실수한-부분)
  - [SELECT 컬럼 구분](#select-컬럼-구분)
  - [세미콜론 위치](#세미콜론-위치)
  - [ORDER BY 사용법](#order-by-사용법)
- [실전 체크](#실전-체크)
  - [동점 정렬 기준 추가](#동점-정렬-기준-추가)
- [오늘 배운 내용](#오늘-배운-내용)


# SQL 기본 문법

## SELECT, FROM

SQL에서 데이터를 조회할 때 가장 기본적인 형태

```sql
SELECT 컬럼명
FROM 테이블명;
```

### 모든 컬럼 조회

`*`을 사용하면 모든 컬럼을 조회할 수 있다.

```sql
SELECT *
FROM STUDENT;
```

### 특정 컬럼 조회

여러 컬럼을 조회할 경우 `,`로 구분한다.

```sql
SELECT NAME, AGE
FROM STUDENT;
```

## WHERE

특정 조건을 만족하는 데이터만 조회할 때 사용한다.

```sql
SELECT NAME, AGE
FROM STUDENT
WHERE AGE >= 20;
```

### 비교 연산자

| 연산자 | 의미 |
| --- | --- |
| `=` | 같다 |
| `<>` | 같지 않다 |
| `>` | 초과 |
| `>=` | 이상 |
| `<` | 미만 |
| `<=` | 이하 |

## AND, OR

여러 조건을 함께 사용할 때 사용한다.

### AND

두 조건을 모두 만족해야 한다.

```sql
SELECT NAME, AGE
FROM STUDENT
WHERE AGE >= 20
AND DEPT = '컴퓨터공학과';
```

### OR

두 조건 중 하나만 만족해도 된다.

```sql
SELECT NAME
FROM STUDENT
WHERE DEPT = '컴퓨터공학과'
OR AGE >= 20;
```

- `AND` → 조건을 모두 만족
- `OR` → 하나라도 만족

`AND`와 `OR`를 함께 사용하면 `AND`가 먼저 계산된다. 조건을 명확히 구분하려면 괄호를 사용한다.

```sql
SELECT NAME, AGE
FROM STUDENT
WHERE (DEPT = '컴퓨터공학과' OR DEPT = '수학과')
AND AGE >= 20;
```

## BETWEEN

특정 범위에 해당하는 데이터를 조회할 때 사용한다.

```sql
SELECT NAME
FROM STUDENT
WHERE AGE BETWEEN 20 AND 25;
```

`BETWEEN 20 AND 25`는 다음과 같은 의미이다.

```text
20 <= AGE <= 25
```

즉, 양 끝값을 포함한다.

```sql
WHERE AGE BETWEEN 20 AND 25
```

는

```sql
WHERE AGE >= 20
AND AGE <= 25
```

와 같은 의미이다.

## IN

여러 값 중 하나에 해당하는 데이터를 조회할 때 사용한다.

```sql
SELECT NAME
FROM STUDENT
WHERE DEPT IN ('컴퓨터공학과', '수학과');
```

다음과 같은 의미이다.

```sql
WHERE DEPT = '컴퓨터공학과'
OR DEPT = '수학과'
```

## LIKE

문자열의 특정 패턴을 검색할 때 사용한다.

### 여러 글자 와일드카드

`%`는 0개 이상의 문자를 의미한다.

```sql
SELECT NAME
FROM STUDENT
WHERE NAME LIKE '김%';
```

→ `김`으로 시작하는 이름

```sql
SELECT NAME
FROM STUDENT
WHERE NAME LIKE '%민%';
```

→ `민`이 포함된 이름

```sql
SELECT NAME
FROM STUDENT
WHERE NAME LIKE '%수';
```

→ `수`로 끝나는 이름

### 한 글자 와일드카드

`_`는 정확히 한 개의 문자를 의미한다.

```sql
NAME LIKE '김_'
```

→ `김` + 한 글자로 이루어진 이름

### 두 와일드카드 비교

- `%` → 0개 이상의 문자
- `_` → 정확히 1개의 문자

## ORDER BY

조회 결과를 특정 컬럼을 기준으로 정렬할 때 사용한다.

```sql
SELECT NAME, AGE
FROM STUDENT
ORDER BY AGE ASC;
```

### 정렬 방향

- `ASC` → 오름차순
- `DESC` → 내림차순

```sql
SELECT NAME, AGE
FROM STUDENT
ORDER BY AGE DESC;
```

→ 나이가 많은 순서

`ASC`는 생략할 수 있으며 기본값은 오름차순이다.


# 궁금증

## 문자열에 작은따옴표를 사용하는 이유

SQL에서는 문자열을 표현할 때 일반적으로 작은따옴표 `' '`를 사용한다.

```sql
WHERE NAME = '김민수'
```

숫자 데이터는 따옴표 없이 사용한다.

```sql
WHERE AGE >= 20
```

큰따옴표 `"`는 SQL 표준에서 문자열보다는 식별자(identifier)를 표현하는 용도로 사용된다. MariaDB/MySQL에서는 설정에 따라 큰따옴표가 문자열로 동작할 수도 있지만, SQL 표준을 따르고 다른 DBMS와의 호환성을 높이기 위해 문자열에는 작은따옴표를 사용하는 것이 안전하다.

따라서 SQL에서는 문자열에 작은따옴표를 사용하는 습관을 들이는 것이 좋다.


# 실수한 부분

## SELECT 컬럼 구분

여러 컬럼을 조회할 때는 `,`로 구분해야 한다.

```sql
SELECT NAME, AGE
FROM STUDENT;
```

## 세미콜론 위치

세미콜론 `;`은 SQL 문장의 끝을 의미한다.

따라서 `WHERE` 앞에 세미콜론을 사용하면 안 된다.

```sql
-- 잘못된 예
SELECT NAME
FROM STUDENT;
WHERE AGE >= 20;
```

```sql
-- 올바른 예
SELECT NAME
FROM STUDENT
WHERE AGE >= 20;
```

## ORDER BY 사용법

`DESC` 또는 `ASC`만 작성하는 것이 아니라 정렬 기준이 되는 컬럼을 함께 작성해야 한다.

```sql
-- 잘못된 예
ORDER BY DESC;
```

```sql
-- 올바른 예
ORDER BY AGE DESC;
```


# 실전 체크

## 동점 정렬 기준 추가

정렬 기준 컬럼의 값이 같으면 결과 순서는 보장되지 않을 수 있다. 일관된 결과가 필요하면 두 번째 정렬 기준을 추가한다.

```sql
SELECT NAME, AGE
FROM STUDENT
ORDER BY AGE DESC, NAME ASC;
```


# 오늘 배운 내용

```sql
SELECT 컬럼
FROM 테이블
WHERE 조건
ORDER BY 컬럼 ASC/DESC;
```

SQL 문제를 풀 때 문제의 문장을 다음과 같이 나누어 생각하면 SQL을 작성하기 쉽다.

```text
무엇을 조회?   → SELECT
어디에서 조회? → FROM
어떤 조건?     → WHERE
어떻게 정렬?   → ORDER BY
```
