- [JOIN](#join)
    - [STUDENT](#student)
    - [DEPARTMENT](#department)
  - [INNER JOIN](#inner-join)
  - [LEFT JOIN](#left-join)
  - [ON](#on)
  - [ON과 WHERE](#on과-where)
- [JOIN과 GROUP BY](#join과-group-by)
  - [JOIN과 집계 함수](#join과-집계-함수)
  - [JOIN과 HAVING](#join과-having)
- [COUNT(*)와 COUNT(컬럼)](#count와-count컬럼)
- [실수한 부분](#실수한-부분)
  - [테이블명과 컬럼명 구분](#테이블명과-컬럼명-구분)
- [오늘 배운 내용](#오늘-배운-내용)


# JOIN

서로 다른 테이블의 데이터를 연결할 때 사용한다.

### STUDENT

| ID | NAME | AGE | DEPT_ID |
| --- | --- | --- | --- |
| 1 | 김민수 | 22 | 10 |
| 2 | 이지은 | 21 | 20 |
| 3 | 박철수 | 25 | 10 |
| 4 | 최영희 | 19 | 30 |
| 5 | 정수진 | 18 | 40 |

### DEPARTMENT

| DEPT_ID | DEPT_NAME |
| --- | --- |
| 10 | 컴퓨터공학과 |
| 20 | 수학과 |
| 30 | 경영학과 |
| 50 | 생물학과 |

## INNER JOIN

양쪽 테이블에서 조건에 일치하는 데이터만 조회한다.

```sql
SELECT student.name, department.dept_name
FROM student
JOIN department
ON student.dept_id = department.dept_id;
```

`JOIN`은 기본적으로 `INNER JOIN`과 같은 의미로 사용할 수 있다.

`student.dept_id = department.dept_id`에 해당하지 않는 정수진은 결과에서 제외된다.

## LEFT JOIN

왼쪽 테이블의 모든 데이터를 유지하면서 오른쪽 테이블에 일치하는 데이터를 연결한다.

```sql
SELECT student.name, department.dept_name
FROM student
LEFT JOIN department
ON student.dept_id = department.dept_id;
```

정수진처럼 오른쪽 테이블에 대응되는 데이터가 없는 경우, 오른쪽 테이블의 컬럼 값은 `NULL`이 된다.

```text
INNER JOIN → 양쪽에서 일치하는 데이터만
LEFT JOIN  → 왼쪽 데이터는 모두 유지
```

## ON

JOIN할 때 두 테이블을 연결하는 기준을 지정한다.

```sql
ON student.dept_id = department.dept_id
```

→ 두 테이블의 `DEPT_ID`가 같은 행을 연결한다.


## ON과 WHERE

`ON`은 테이블을 연결하기 위한 조건이고, `WHERE`는 JOIN한 결과에서 원하는 행을 필터링하는 조건이다.

```sql
SELECT student.name, department.dept_name
FROM student
JOIN department
ON student.dept_id = department.dept_id
WHERE department.dept_name = '컴퓨터공학과';
```

```text
ON
→ 두 테이블을 어떻게 연결할지

WHERE
→ 연결된 결과 중 어떤 데이터를 남길지
```

`LEFT JOIN`에서 오른쪽 테이블의 조건을 `WHERE`에 작성하면, `NULL`인 행이 제외되어 `INNER JOIN`처럼 보일 수 있다.

```sql
SELECT student.name, department.dept_name
FROM student
LEFT JOIN department
ON student.dept_id = department.dept_id
WHERE department.dept_name = '컴퓨터공학과';
```

위 쿼리에서는 부서가 없는 정수진이 `WHERE` 조건을 만족하지 못해 제외된다.


# JOIN과 GROUP BY

## JOIN과 집계 함수

두 테이블을 연결한 후 `GROUP BY`와 집계 함수를 사용하여 그룹별 통계를 구할 수 있다.

```sql
SELECT department.dept_name, COUNT(*)
FROM student
JOIN department
ON student.dept_id = department.dept_id
GROUP BY department.dept_name;
```

→ 학과별 학생 수

```sql
SELECT department.dept_name, AVG(student.age)
FROM student
JOIN department
ON student.dept_id = department.dept_id
GROUP BY department.dept_name;
```

→ 학과별 평균 나이

## JOIN과 HAVING

JOIN한 결과를 그룹화한 후 집계 결과에 조건을 적용할 수 있다.

```sql
SELECT department.dept_name, AVG(student.age)
FROM student
JOIN department
ON student.dept_id = department.dept_id
GROUP BY department.dept_name
HAVING AVG(student.age) >= 20;
```

→ 학과별 평균 나이가 20세 이상인 학과만 조회


# COUNT(*)와 COUNT(컬럼)

`COUNT(*)`는 행의 개수를 세고, `COUNT(컬럼)`은 해당 컬럼이 `NULL`이 아닌 행의 개수를 센다.

특히 `LEFT JOIN`에서 차이가 발생할 수 있다.

```sql
SELECT department.dept_name, COUNT(student.id)
FROM department
LEFT JOIN student
ON department.dept_id = student.dept_id
GROUP BY department.dept_name;
```

학생이 없는 학과는 `student.id`가 `NULL`이 되므로 `COUNT(student.id)`는 0으로 계산된다.

반면 `COUNT(*)`는 `LEFT JOIN`으로 유지된 생물학과 행까지 세므로 1로 계산된다.

```text
COUNT(*)         → JOIN 결과의 행 개수
COUNT(student.id) → NULL이 아닌 student.id의 개수
```


# 실수한 부분

## 테이블명과 컬럼명 구분

JOIN에서는 같은 컬럼명이 여러 테이블에 존재할 수 있으므로 `테이블명.컬럼명` 형태로 작성하면 어떤 컬럼을 사용하는지 명확하게 구분할 수 있다.

```sql
SELECT student.name, department.dept_name
FROM student
JOIN department
ON student.dept_id = department.dept_id;
```

```text
student.name
→ student 테이블의 name

department.dept_name
→ department 테이블의 dept_name
```

테이블명이 길어지면 별칭(alias)을 사용할 수도 있다.

```sql
SELECT s.name, d.dept_name
FROM student s
JOIN department d
ON s.dept_id = d.dept_id;
```


# 오늘 배운 내용

```text
JOIN
→ 테이블 연결

ON
→ JOIN 기준

INNER JOIN
→ 양쪽에서 일치하는 데이터만

LEFT JOIN
→ 왼쪽 테이블의 데이터는 모두 유지

WHERE
→ 개별 행 필터링

GROUP BY
→ 그룹화

HAVING
→ 그룹 필터링

COUNT
→ 개수
```

JOIN 문제를 풀 때 다음과 같이 생각하면 쉽게 조립할 수 있다.

```text
어떤 데이터를 출력? → SELECT

어떤 테이블을 연결? → JOIN

무엇을 기준으로 연결? → ON

어떤 행을 필터링? → WHERE

어떤 기준으로 그룹화? → GROUP BY

어떤 그룹을 남길지? → HAVING
```
