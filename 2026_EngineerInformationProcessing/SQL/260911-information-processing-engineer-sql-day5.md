- [DISTINCT](#distinct)
- [NULL](#null)
- [CASE](#case)
- [별칭](#별칭)
- [실수한 부분](#실수한-부분)
  - [NULL 비교](#null-비교)
- [오늘 배운 내용](#오늘-배운-내용)


# DISTINCT, NULL, CASE, 별칭

## DISTINCT

조회 결과에서 중복된 값을 제거할 때 사용한다.

```sql
SELECT DISTINCT DEPT
FROM STUDENT;
```

→ 중복되지 않는 학과 목록 조회

Python의 `set()`으로 중복을 제거하는 것과 비슷하게 이해할 수 있다.

## NULL

`NULL`은 값이 없거나 알 수 없는 상태를 의미한다.

`NULL`은 일반적인 `=` 비교가 아니라 `IS NULL`, `IS NOT NULL`을 사용한다.

```sql
SELECT NAME
FROM STUDENT
WHERE AGE IS NULL;
```

→ 나이가 입력되지 않은 학생

```sql
SELECT NAME
FROM STUDENT
WHERE AGE IS NOT NULL;
```

→ 나이가 입력된 학생

잘못된 형태:

```sql
WHERE AGE = NULL;
```

## CASE

조건에 따라 다른 값을 출력할 때 사용한다.

```sql
SELECT NAME, AGE,
       CASE
           WHEN AGE IS NULL THEN '미입력'
           WHEN AGE >= 20 THEN '성인'
           ELSE '미성년자'
       END AS STATUS
FROM STUDENT;
```

`AGE`가 `NULL`이면 `AGE >= 20`의 결과도 참이 아니므로, 먼저 `NULL`을 처리해야 미성년자로 잘못 분류하지 않는다.

기본 형태:

```text
CASE
    WHEN 조건 THEN 결과
    ELSE 결과
END
```

## 별칭

`AS`를 사용하여 컬럼이나 테이블에 별칭을 지정할 수 있다.

```sql
CASE
    WHEN AGE >= 20 THEN '성인'
    ELSE '미성년자'
END AS STATUS
```

→ `CASE`로 계산한 결과 컬럼의 이름을 `STATUS`로 지정

테이블에도 별칭을 사용할 수 있다.

```sql
SELECT s.NAME, d.DEPT_NAME
FROM STUDENT AS s
JOIN DEPARTMENT AS d
ON s.DEPT_ID = d.DEPT_ID;
```

`AS`는 생략할 수도 있다.

```sql
FROM STUDENT s
```

# 실수한 부분

## NULL 비교

`NULL` 데이터를 찾을 때 `IS NULL`을 사용한다.

```sql
-- 잘못된 예
WHERE AGE IS NOT NULL;
```

문제에서 "나이가 입력되지 않은 학생"을 찾는 경우에는:

```sql
-- 올바른 예
WHERE AGE IS NULL;
```

`IS NOT NULL`은 반대로 값이 존재하는 데이터를 조회한다.

# 오늘 배운 내용

```text
DISTINCT
→ 중복 제거

NULL
→ IS NULL / IS NOT NULL

CASE
→ 조건에 따라 다른 값 반환

AS
→ 컬럼이나 테이블의 별칭 지정
```

오늘 SQL은 지금까지 배운 기본 문법에 새로운 기능을 추가한 내용이다.

```text
SELECT
WHERE
GROUP BY
HAVING
ORDER BY
JOIN
서브쿼리
DISTINCT
NULL
CASE
```
