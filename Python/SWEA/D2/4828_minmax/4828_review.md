- [총평](#총평)
- [보완점](#보완점)
  - [1. 입력 처리 속도 최적화](#1-입력-처리-속도-최적화)
  - [2. 출력 처리 최적화](#2-출력-처리-최적화)
- [최종 코드 예시](#최종-코드-예시)


# 총평
- 문제 요구사항을 정확히 충족하며, 정상적으로 동작합니다.
- 내장 함수 `min`과 `max`를 활용하여 간결하게 구현되었습니다.
- f-string을 사용해 출력 형식을 명확하고 직관적으로 표현했습니다.

# 보완점
## 1. 입력 처리 속도 최적화
대량의 입력이 들어오는 환경에서는 `sys.stdin.readline`을 사용해 입력 속도를 개선할 수 있습니다.
```python
import sys
input = sys.stdin.readline
```

## 2. 출력 처리 최적화
매번 `print`를 호출하는 대신, 결과를 리스트에 모아 한 번에 출력하면 I/O 오버헤드를 줄일 수 있습니다.
```python
answers = []
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    answers.append(f'#{test_case} {max(nums) - min(nums)}')
print('\n'.join(answers))
```

# 최종 코드 예시
```python
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    answers = []
    for test_case in range(1, T + 1):
        _ = int(input())  # 리스트 크기 정보 (사용하지 않지만 읽어들임)
        nums = list(map(int, input().split()))
        answers.append(f'#{test_case} {max(nums) - min(nums)}')
    print('\n'.join(answers))

if __name__ == '__main__':
    main()
```