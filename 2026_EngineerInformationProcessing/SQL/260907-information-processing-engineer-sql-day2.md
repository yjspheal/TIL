- [집계 함수](#집계-함수)
  - [COUNT, SUM, AVG, MAX, MIN](#count-sum-avg-max-min)
- [GROUP BY](#group-by)
  - [GROUP BY와 집계 함수](#group-by와-집계-함수)
  - [SELECT에서 사용 가능한 컬럼](#select에서-사용-가능한-컬럼)
- [HAVING](#having)
- [WHERE와 HAVING](#where와-having)
- [실수한 부분](#실수한-부분)
  - [GROUP BY 사용법](#group-by-사용법)
  - [ORDER BY 사용법](#order-by-사용법)
- [오늘 배운 내용](#오늘-배운-내용)


# 집계 함수

여러 행의 데이터를 계산하여 하나의 값으로 반환한다.

## COUNT, SUM, AVG, MAX, MIN

```text
COUNT → 개수
SUM   → 합계
AVG   → 평균
MAX   → 최댓값
MIN   → 최솟값
```

```sql
SELECT COUNT(*)
FROM STUDENT;

SELECT SUM(AGE)
FROM STUDENT;

SELECT AVG(AGE)
FROM STUDENT;

SELECT MAX(AGE)
FROM STUDENT;

SELECT MIN(AGE)
FROM STUDENT;
```

`COUNT(*)`는 전체 행의 수를 세고, `COUNT(컬럼명)`은 해당 컬럼의 값이 `NULL`이 아닌 행만 센다.

```sql
SELECT COUNT(*)
FROM STUDENT;

SELECT COUNT(AGE)
FROM STUDENT;
```

`SUM`, `AVG`, `MAX`, `MIN`도 일반적으로 `NULL` 값을 제외하고 계산한다.

# GROUP BY

특정 컬럼을 기준으로 데이터를 그룹화할 때 사용한다.

## GROUP BY와 집계 함수

`GROUP BY`와 집계 함수를 함께 사용하면 그룹별 통계 값을 구할 수 있다.

```sql
SELECT DEPT, COUNT(*), AVG(AGE)
FROM STUDENT
GROUP BY DEPT;
```

→ 학과별 학생 수와 평균 나이

## SELECT에서 사용 가능한 컬럼

`GROUP BY`를 사용하는 경우 `SELECT`에는 기본적으로 그룹 기준 컬럼과 집계 함수가 사용된다.

```sql
SELECT DEPT, MAX(AGE)
FROM STUDENT
GROUP BY DEPT;
```

```sql
SELECT DEPT, AGE
FROM STUDENT
GROUP BY DEPT;
```

위 쿼리는 `DEPT` 하나의 그룹에 여러 `AGE`가 존재할 수 있기 때문에, 엄격한 SQL 기준에서는 적절하지 않다. DBMS 설정에 따라 실행되더라도 어떤 `AGE`가 조회될지는 보장되지 않는다.


# HAVING

`GROUP BY`로 그룹화한 결과에 조건을 적용할 때 사용한다.

```sql
SELECT DEPT, COUNT(*)
FROM STUDENT
GROUP BY DEPT
HAVING COUNT(*) >= 2;
```

→ 학생 수가 2명 이상인 학과만 조회


# WHERE와 HAVING

```text
WHERE  → 개별 행에 조건
HAVING → 그룹에 조건
```

예를 들어 20세 이상인 학생만 대상으로 학과별 평균 나이를 구하려면:

```sql
SELECT DEPT, AVG(AGE)
FROM STUDENT
WHERE AGE >= 20
GROUP BY DEPT;
```

학과별 평균 나이가 20세 이상인 학과만 조회하려면:

```sql
SELECT DEPT, AVG(AGE)
FROM STUDENT
GROUP BY DEPT
HAVING AVG(AGE) >= 20;
```

`WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`를 함께 사용하면 다음과 같다.

```sql
SELECT DEPT, COUNT(*), AVG(AGE)
FROM STUDENT
WHERE AGE >= 20
GROUP BY DEPT
HAVING COUNT(*) >= 2
ORDER BY COUNT(*) DESC, DEPT ASC;
```


# 실수한 부분

## GROUP BY 사용법

`GROUP BY`는 조건을 작성하는 부분이 아니므로 `=`을 사용하지 않는다.

```sql
-- 잘못된 예
GROUP BY = 'DEPT'
```

```sql
-- 올바른 예
GROUP BY DEPT;
```

## ORDER BY 사용법

정렬 시 `SORT BY`가 아니라 `ORDER BY`를 사용한다.

```sql
-- 잘못된 예
SELECT DEPT, COUNT(*)
FROM STUDENT
GROUP BY DEPT
SORT BY COUNT(*) DESC;
```

```sql
-- 올바른 예
SELECT DEPT, COUNT(*)
FROM STUDENT
GROUP BY DEPT
ORDER BY COUNT(*) DESC;
```


# 오늘 배운 내용

```text
집계 함수
COUNT / SUM / AVG / MAX / MIN

GROUP BY
→ 데이터를 그룹별로 묶기

WHERE
→ 개별 행에 조건

HAVING
→ 그룹에 조건

ORDER BY
→ 결과 정렬
```

SQL 작성 시 다음과 같이 생각하면 쉽다.

```text
FROM
  ↓
WHERE
  ↓
GROUP BY
  ↓
HAVING
  ↓
SELECT
  ↓
ORDER BY
```
