- [총평](#총평)
- [보완점](#보완점)
  - [1. 모드 계산 로직 간결화](#1-모드-계산-로직-간결화)
- [최종 코드 예시](#최종-코드-예시)



# 총평
- 문제 요구사항(최빈수 구하기 및 최대 점수 선택)을 정확히 충족합니다.  
- 점수 분포를 리스트로 집계하여 빈도 계산을 효율적으로 처리했습니다.  
- `filter`와 `max` 조합으로 빈도가 가장 높은 점수를 올바르게 선택합니다.  

<br>

# 보완점
## 1. 모드 계산 로직 간결화
`filter`와 별도의 리스트 생성 대신, `max` 함수의 `key` 매개변수를 활용해 한 줄로 최빈수(빈도, 점수 기준)를 계산할 수 있습니다.
```python
mode = max(range(101), key=lambda x: (scores[x], x))
```

<br>


# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        _ = int(input())  # 점수 개수(사용하지 않지만 읽어들임)
        scores = [0] * 101
        for score in map(int, input().split()):
            scores[score] += 1
        # (빈도, 점수) 기준으로 최빈수 계산
        mode = max(range(101), key=lambda x: (scores[x], x))
        print(f'#{test_case} {mode}')

if __name__ == '__main__':
    main()
```
