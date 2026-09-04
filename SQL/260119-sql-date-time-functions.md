# SQL 실습 Day 4 — 시간 조건(>=, <, BETWEEN) + 최근 N건(ORDER BY + LIMIT) 10분 컷

## 목차
- [SQL 실습 Day 4 — 시간 조건(\>=, \<, BETWEEN) + 최근 N건(ORDER BY + LIMIT) 10분 컷](#sql-실습-day-4--시간-조건--between--최근-n건order-by--limit-10분-컷)
  - [목차](#목차)
  - [Day 4 목표](#day-4-목표)
  - [실습 데이터 세팅](#실습-데이터-세팅)
  - [1. `>=` : 특정 시각 이후(포함)](#1---특정-시각-이후포함)
    - [목표](#목표)
    - [결과](#결과)
  - [2. `<` : 특정 시각 이전(미포함)](#2---특정-시각-이전미포함)
    - [목표](#목표-1)
    - [결과](#결과-1)
  - [3. `BETWEEN` : 구간 조회(양끝 포함)](#3-between--구간-조회양끝-포함)
    - [목표](#목표-2)
    - [결과](#결과-2)
  - [4. `ORDER BY + LIMIT` : 가장 최근 N건](#4-order-by--limit--가장-최근-n건)
    - [목표](#목표-3)
    - [결과](#결과-3)
  - [오늘 결과 요약](#오늘-결과-요약)
  - [Day 4 회고](#day-4-회고)
  - [다음 계획 (Day 5)](#다음-계획-day-5)

---

## Day 4 목표
- `event_time`을 기준으로 **시간 범위 조건 조회**하기
  - `>=` (이후, 포함)
  - `<` (이전, 미포함)
  - `BETWEEN` (구간, 보통 양끝 포함)
- `ORDER BY + LIMIT`로 **최근 N건 패턴** 만들기

설치/접속 이슈를 해결하느라 시간이 늦어져, 오늘은 **핵심만 빠르게(10분 컷)** 진행했다

---

## 실습 데이터 세팅

~~~~sql
CREATE DATABASE IF NOT EXISTS sql_practice
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE sql_practice;

CREATE TABLE IF NOT EXISTS event_logs (
  user_id INT,
  event_type VARCHAR(50),
  event_time DATETIME,
  device TEXT
);

TRUNCATE TABLE event_logs;

INSERT INTO event_logs VALUES
(1, 'view',  '2026-01-14 09:55:00', 'mobile'),
(1, 'click', '2026-01-14 09:56:10', 'mobile'),
(2, 'view',  '2026-01-14 10:01:00', 'pc');
~~~~

---

## 1. `>=` : 특정 시각 이후(포함)

### 목표
`2026-01-14 09:56:00` **이후(포함)** 발생한 이벤트만 조회

~~~~sql
SELECT *
FROM event_logs
WHERE event_time >= '2026-01-14 09:56:00';
~~~~

### 결과
- **2건**

---

## 2. `<` : 특정 시각 이전(미포함)

### 목표
`2026-01-14 10:00:00` **이전(미포함)** 이벤트만 조회

~~~~sql
SELECT *
FROM event_logs
WHERE event_time < '2026-01-14 10:00:00';
~~~~

### 결과
- **2건**

---

## 3. `BETWEEN` : 구간 조회(양끝 포함)

### 목표
`09:55:00` ~ `10:00:00` **사이(보통 양끝 포함)** 이벤트 조회

~~~~sql
SELECT *
FROM event_logs
WHERE event_time BETWEEN '2026-01-14 09:55:00'
                     AND '2026-01-14 10:00:00';
~~~~

### 결과
- **2건**

> 참고: MariaDB/MySQL에서 `BETWEEN`은 일반적으로 양끝 값을 포함(inclusive)하는 형태로 동작한다

---

## 4. `ORDER BY + LIMIT` : 가장 최근 N건

### 목표
가장 최근 이벤트 **1건**만 조회

~~~~sql
SELECT *
FROM event_logs
ORDER BY event_time DESC
LIMIT 1;
~~~~

### 결과
- **1건**

---

## 오늘 결과 요약

- `>= '2026-01-14 09:56:00'` → **2건**
- `<  '2026-01-14 10:00:00'` → **2건**
- `BETWEEN '09:55:00' AND '10:00:00'` → **2건**
- `ORDER BY event_time DESC LIMIT 1` → **1건**

---

## Day 4 회고
- 시간 조건은 `>= / < / BETWEEN` 조합으로 범위를 만들 수 있다
- “최근 N건”은 결국 `ORDER BY ... DESC`와 `LIMIT N`의 결합이다
- 설치/접속 문제를 해결한 덕분에, 이후 실습은 반복 실행이 쉬워졌다

---

## 다음 계획 (Day 5)
- `GROUP BY` + `COUNT(*)`로 집계하기
- 예: `device`별 이벤트 개수, `event_type`별 발생 횟수