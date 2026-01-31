# SQL 실습 Day 6 — HAVING & COUNT(DISTINCT)로 “집계 결과를 거르기”

## 목차
- [SQL 실습 Day 6 — HAVING \& COUNT(DISTINCT)로 “집계 결과를 거르기”](#sql-실습-day-6--having--countdistinct로-집계-결과를-거르기)
  - [목차](#목차)
  - [Day 6 목표](#day-6-목표)
  - [실습 데이터 재세팅](#실습-데이터-재세팅)
  - [1. HAVING으로 집계 결과 필터링](#1-having으로-집계-결과-필터링)
    - [결과](#결과)
  - [2. WHERE vs HAVING 다시 정리](#2-where-vs-having-다시-정리)
  - [3. COUNT(DISTINCT)로 중복 제거 집계](#3-countdistinct로-중복-제거-집계)
    - [결과](#결과-1)
  - [4. HAVING + DISTINCT 조합](#4-having--distinct-조합)
    - [결과](#결과-2)
  - [오늘의 포인트 정리](#오늘의-포인트-정리)
  - [Day 6 회고](#day-6-회고)
  - [다음 방향](#다음-방향)

---

## Day 6 목표
- 집계 결과에 조건을 거는 `HAVING` 이해하기
- `WHERE`와 `HAVING`의 역할 차이 구분하기
- `COUNT(DISTINCT ...)`로 “서로 다른 값” 기준 집계하기

---

## 실습 데이터 재세팅
다른 노트북 환경이라 데이터를 다시 맞춰주고 진행했다
(Day 5와 동일한 20개 데이터)

~~~~sql
USE sql_practice;

TRUNCATE TABLE event_logs;

INSERT INTO event_logs (user_id, event_type, event_time, device) VALUES
(1, 'view',     '2026-01-14 09:50:12', 'mobile'),
(2, 'click',    '2026-01-14 09:51:33', 'pc'),
(3, 'purchase', '2026-01-14 09:52:05', 'tablet'),
(4, 'view',     '2026-01-14 09:53:47', 'pc'),
(5, 'click',    '2026-01-14 09:54:21', 'mobile'),

(1, 'purchase', '2026-01-14 09:55:08', 'pc'),
(2, 'view',     '2026-01-14 09:56:49', 'tablet'),
(3, 'click',    '2026-01-14 09:57:14', 'mobile'),
(4, 'purchase', '2026-01-14 09:58:30', 'tablet'),
(5, 'view',     '2026-01-14 09:59:55', 'mobile'),

(2, 'click',    '2026-01-14 10:00:11', 'pc'),
(3, 'view',     '2026-01-14 10:01:26', 'tablet'),
(1, 'click',    '2026-01-14 10:02:44', 'tablet'),
(4, 'view',     '2026-01-14 10:03:09', 'mobile'),
(5, 'purchase', '2026-01-14 10:04:37', 'pc'),

(1, 'view',     '2026-01-14 10:05:58', 'tablet'),
(2, 'purchase', '2026-01-14 10:06:22', 'mobile'),
(3, 'click',    '2026-01-14 10:07:41', 'pc'),
(4, 'purchase', '2026-01-14 10:08:16', 'mobile'),
(5, 'click',    '2026-01-14 10:09:45', 'tablet');
~~~~

---

## 1. HAVING으로 집계 결과 필터링
device별 이벤트 개수를 구한 뒤,
**개수가 일정 기준 이상인 것만** 보고 싶어졌다

처음에는 조건을 걸었는데 **아무 행도 나오지 않았다**
문법 오류가 아니라, **데이터가 조건을 만족하지 못한 상황**이었다

기준을 다시 맞춘 뒤 실행:

~~~~sql
SELECT device, COUNT(*) AS cnt
FROM event_logs
GROUP BY device
HAVING cnt >= 3;
~~~~

### 결과
- **3행** (mobile / pc / tablet)

---

## 2. WHERE vs HAVING 다시 정리
오늘 가장 중요한 개념

- `WHERE`
  → **집계 전에** 개별 행을 필터링
- `HAVING`
  → **집계 후에** 그룹 결과를 필터링

> “COUNT 결과에 조건을 걸고 싶다”
→ 무조건 `HAVING`

---

## 3. COUNT(DISTINCT)로 중복 제거 집계
이번에는 이벤트 개수가 아니라,

> device별로 **서로 다른 사용자 수**를 보고 싶었다

~~~~sql
SELECT device, COUNT(DISTINCT user_id) AS uniq_users
FROM event_logs
GROUP BY device
ORDER BY uniq_users DESC;
~~~~

### 결과
- mobile / pc / tablet 모두 **5**

처음엔 이상하게 느껴졌지만,
데이터 자체가 모든 device에 user_id 1~5가 전부 등장하도록 설계되어 있었기 때문에
**자연스러운 결과**였다

---

## 4. HAVING + DISTINCT 조합
중복 제거 집계 결과에도 조건을 걸어봤다

~~~~sql
SELECT device, COUNT(DISTINCT user_id) AS uniq_users
FROM event_logs
GROUP BY device
HAVING uniq_users = 5;
~~~~

### 결과
- **3행**

`HAVING`은 단순 `COUNT(*)`뿐 아니라
`COUNT(DISTINCT ...)` 같은 집계 함수에도 그대로 적용 가능함을 확인했다

---

## 오늘의 포인트 정리
- `HAVING` = **집계 결과에 거는 WHERE**
- `COUNT(DISTINCT col)` = **중복 제거 후 집계**
- 결과가 전부 같다면?
  - 쿼리보다 **데이터 분포를 먼저 확인**

---

## Day 6 회고
- 문법보다 “이 조건이 집계 전인지, 후인지”를 구분하는 사고가 더 중요했다
- SQL이 점점 “문법 암기”가 아니라
  **데이터를 어떻게 요약하고 해석할지**의 문제로 느껴지기 시작했다
- 다음부터는 정답을 바로 받기보다,
  문제를 먼저 던지고 직접 풀어보는 방식이 더 잘 맞을 것 같다는 것도 깨달았다

---

## 다음 방향
- Day 7: `CASE WHEN`으로 조건부 집계
- 또는 `GROUP BY` 결과를 피벗처럼 해석하는 연습
- 진행 방식은 **힌트 최소, 직접 작성 위주**로 전환