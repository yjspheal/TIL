# SQL 실습 Day 3 — AND/OR 우선순위와 괄호, IN으로 조건을 안전하게 만들기

## 목차
- [SQL 실습 Day 3 — AND/OR 우선순위와 괄호, IN으로 조건을 안전하게 만들기](#sql-실습-day-3--andor-우선순위와-괄호-in으로-조건을-안전하게-만들기)
  - [목차](#목차)
  - [Day 3 목표](#day-3-목표)
  - [오늘의 핵심 한 줄](#오늘의-핵심-한-줄)
  - [1. AND 조건으로 교집합 만들기](#1-and-조건으로-교집합-만들기)
    - [목표](#목표)
    - [처음 시도 (실수: 따옴표/식별자 혼동)](#처음-시도-실수-따옴표식별자-혼동)
    - [문제점](#문제점)
    - [수정 후 (MariaDB/MySQL에서 안전한 형태)](#수정-후-mariadbmysql에서-안전한-형태)
  - [2. OR를 섞었을 때 괄호가 선택인 경우](#2-or를-섞었을-때-괄호가-선택인-경우)
    - [목표(의도)](#목표의도)
  - [3. 괄호가 필수가 되는 케이스](#3-괄호가-필수가-되는-케이스)
    - [목표(의도)](#목표의도-1)
    - [괄호 포함 (의도대로 동작)](#괄호-포함-의도대로-동작)
    - [괄호 제거 (결과가 달라짐)](#괄호-제거-결과가-달라짐)
  - [4. IN으로 OR를 더 안전하게 쓰기](#4-in으로-or를-더-안전하게-쓰기)
  - [Day 3 회고](#day-3-회고)
  - [다음 계획 (Day 4)](#다음-계획-day-4)

---

## Day 3 목표
- 조건 여러 개를 조합해서 조회하기 (`AND`, `OR`)
- 연산 우선순위를 이해하고 필요한 곳에 괄호(`()`) 적용하기
- `OR` 반복을 `IN (...)`으로 안전하게 대체하기

사용 테이블: `event_logs`

---

## 오늘의 핵심 한 줄
> 괄호를 빼면 **연산 우선순위** 때문에 결과가 달라진다

---

## 1. AND 조건으로 교집합 만들기

### 목표
`mobile` 기기이면서(`AND`) `view` 이벤트인 행만 조회

### 처음 시도 (실수: 따옴표/식별자 혼동)
~~~~sql
SELECT * FROM event_logs
WHERE "device" = "mobile"
  AND "event_type" = "view";
~~~~

### 문제점
- MariaDB/MySQL에서는 문자열 값은 **작은따옴표**가 안전한 표준
- 컬럼명도 보통은 **그냥** 쓰며, 식별자를 감쌀 때는 MySQL 계열에서 **백틱(`)** 을 사용
- 큰따옴표(`" "`)는 설정에 따라 동작이 애매해져 **에러 없이 0건**이 나오는 등 혼동을 유발할 수 있음

### 수정 후 (MariaDB/MySQL에서 안전한 형태)
~~~~sql
SELECT *
FROM event_logs
WHERE device = 'mobile'
  AND event_type = 'view';
~~~~

---

## 2. OR를 섞었을 때 괄호가 선택인 경우

### 목표(의도)
`(mobile AND view) OR pc`

~~~~sql
SELECT *
FROM event_logs
WHERE device = 'mobile'
  AND event_type = 'view'
   OR device = 'pc';
~~~~

이 케이스는 `AND`가 `OR`보다 우선이라서, SQL이 아래처럼 해석한다

~~~~
(device = 'mobile' AND event_type = 'view') OR device = 'pc'
~~~~

결과도 의도대로 나왔다

---

## 3. 괄호가 필수가 되는 케이스

### 목표(의도)
`(mobile OR pc) AND view`

즉, device는 mobile/pc만 허용하되, event_type은 view인 것만 보고 싶다

### 괄호 포함 (의도대로 동작)
~~~~sql
SELECT *
FROM event_logs
WHERE (device = 'mobile' OR device = 'pc')
  AND event_type = 'view';
~~~~

### 괄호 제거 (결과가 달라짐)
괄호를 빼고 실행했더니 결과가 **3건으로 증가**했다

이유는 SQL이 다음처럼 해석하기 때문이다

~~~~
device='mobile' OR (device='pc' AND event_type='view')
~~~~

즉 `device='mobile'` 인 행은 event_type과 무관하게 포함되어
`mobile + click` 같은 행이 끼어들 수 있다

---

## 4. IN으로 OR를 더 안전하게 쓰기

`device = 'mobile' OR device = 'pc'` 처럼 OR가 반복되는 패턴은 `IN (...)`으로 대체하면 짧고 안전하다

~~~~sql
SELECT *
FROM event_logs
WHERE device IN ('mobile', 'pc')
  AND event_type = 'view';
~~~~

- 의도 전달이 명확해지고
- 괄호/우선순위 실수 가능성이 줄어든다

---

## Day 3 회고
- `AND` / `OR` 자체보다 더 중요한 건 **우선순위와 괄호로 의도를 고정하는 것**
- 에러 없이 결과가 달라질 수 있어서, 특히 `OR`가 섞일 때는 **의도한 그룹을 반드시 괄호로 묶는 습관**이 필요
- 반복되는 `OR`는 `IN (...)`으로 바꾸면 실수를 크게 줄일 수 있음

---

## 다음 계획 (Day 4)
- `BETWEEN`, `>=`, `<` 로 시간 범위 조건 만들기 (`event_time` 활용)
- `ORDER BY` + `LIMIT`을 다시 결합해서 “최근 N건” 패턴 만들기
- (선택) 실행 순서/성능 관점에서 `WHERE` → `ORDER BY` → `LIMIT` 다시 점검