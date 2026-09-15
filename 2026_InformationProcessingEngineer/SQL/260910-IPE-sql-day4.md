- [서브쿼리](#서브쿼리)
  - [서브쿼리 기본 구조](#서브쿼리-기본-구조)
  - [비교 연산자와 서브쿼리](#비교-연산자와-서브쿼리)
  - [IN과 서브쿼리](#in과-서브쿼리)
  - [중첩 서브쿼리](#중첩-서브쿼리)
- [실수한 부분](#실수한-부분)
  - [MAX와 서브쿼리 사용](#max와-서브쿼리-사용)
- [오늘 배운 내용](#오늘-배운-내용)


# 서브쿼리

SQL문 안에 다른 SQL문을 작성하는 것을 서브쿼리라고 한다.

서브쿼리에서 먼저 값을 구한 후, 그 결과를 바깥 쿼리에서 사용할 수 있다.


## 서브쿼리 기본 구조

전체 학생의 평균 나이보다 나이가 많은 학생을 조회할 수 있다.

```sql
SELECT NAME, AGE
FROM STUDENT
WHERE AGE > (
    SELECT AVG(AGE)
    FROM STUDENT
);
```

안쪽 서브쿼리에서 평균 나이를 먼저 계산한 후, 바깥 쿼리에서 해당 값과 비교한다.

```text
서브쿼리 실행
→ 평균 나이 계산

바깥 쿼리
→ 평균보다 나이가 많은 학생 조회
```


## 비교 연산자와 서브쿼리

서브쿼리가 하나의 값을 반환하는 경우 `=`, `>`, `<`, `>=`, `<=` 등의 비교 연산자와 함께 사용할 수 있다.

```sql
SELECT NAME
FROM STUDENT
WHERE AGE = (
    SELECT MAX(AGE)
    FROM STUDENT
);
```

→ 가장 나이가 많은 학생의 이름


## IN과 서브쿼리

서브쿼리가 하나 이상의 값을 반환할 수 있는 경우 `IN`을 사용할 수 있다.

```sql
SELECT NAME
FROM STUDENT
WHERE DEPT_ID IN (
    SELECT DEPT_ID
    FROM DEPARTMENT
    WHERE DEPT_NAME = '컴퓨터공학과'
);
```

안쪽 서브쿼리에서 컴퓨터공학과의 `DEPT_ID`를 가져온 후, 해당 `DEPT_ID`를 가진 학생을 조회한다.


## 중첩 서브쿼리

서브쿼리 안에 또 다른 서브쿼리를 사용할 수도 있다.

```sql
SELECT NAME, AGE
FROM STUDENT
WHERE AGE > (
    SELECT AVG(AGE)
    FROM STUDENT
    WHERE DEPT_ID = (
        SELECT DEPT_ID
        FROM DEPARTMENT
        WHERE DEPT_NAME = '컴퓨터공학과'
    )
);
```

실행 과정을 단계별로 생각하면 이해하기 쉽다.

```text
① 컴퓨터공학과의 DEPT_ID 조회
        ↓
② 해당 학과 학생들의 평균 나이 계산
        ↓
③ 평균보다 나이가 많은 학생 조회
```


# 실수한 부분

## MAX와 서브쿼리 사용

`MAX()`를 서브쿼리 안에서 사용하면 결과값 하나를 반환하므로, 바깥 쿼리에서 비교할 수 있다.

잘못된 형태:

```sql
WHERE AGE = MAX(
    SELECT MAX(AGE)
    FROM STUDENT
);
```

올바른 형태:

```sql
WHERE AGE = (
    SELECT MAX(AGE)
    FROM STUDENT
);
```

`MAX()` 자체를 바깥쪽에서 한 번 더 사용할 필요가 없다.

서브쿼리의 결과인 최댓값과 `AGE`를 비교하면 된다.


# 오늘 배운 내용

```text
서브쿼리
→ SQL문 안에 SQL문 작성

단일 값 반환
→ =, >, < 등의 비교 연산자와 사용

여러 값 반환
→ IN과 사용

중첩 서브쿼리
→ 서브쿼리 안에 또 다른 서브쿼리
```

서브쿼리의 결과 개수에 따라 연산자를 선택한다.

```text
결과가 하나
→ =, >, < 등의 비교 연산자

결과가 하나 이상
→ IN
```

서브쿼리 문제를 풀 때는 먼저 **바깥 쿼리가 필요로 하는 값을 서브쿼리에서 구한다**고 생각하면 된다.

```text
무엇을 비교할까?
→ 서브쿼리로 기준값 계산

그 기준값을 이용해
→ 바깥 쿼리에서 원하는 데이터 조회
```
