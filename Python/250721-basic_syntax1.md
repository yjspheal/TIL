- [심화학습](#심화학습)
  - [f-string advanced](#f-string-advanced)
    - [활용 1 - upper, lower](#활용-1---upper-lower)
    - [활용 2 - 변수 호출 가능](#활용-2---변수-호출-가능)
    - [활용 3 - 정렬 가능](#활용-3---정렬-가능)
    - [활용 4 - if/else문 적용 가능](#활용-4---ifelse문-적용-가능)
    - [활용 5 - 연산 가능](#활용-5---연산-가능)
    - [활용 6 - 정수 출력 자리수 지정 가능](#활용-6---정수-출력-자리수-지정-가능)
    - [활용 7 - 소수점 출력 자리수 지정 가능](#활용-7---소수점-출력-자리수-지정-가능)
    - [활용 8 - 긴 정수 사이 구분 기호 추가](#활용-8---긴-정수-사이-구분-기호-추가)
    - [활용 9 - 날짜 출력 방식 선택 가능](#활용-9---날짜-출력-방식-선택-가능)


# 심화학습
## f-string advanced
### 활용 1 - upper, lower
- 대/소문자화 가능
```python
msg = f'Hi, my name is {family_name.upper()} {given_name.lower()}
```

### 활용 2 - 변수 호출 가능
- 딕셔너리 타입의 변수를 호출해서 문자열에 직접 포함시킬 수 있다.
```python
info = {'name': 'Claire', 'city': 'Seoul'}
msg = f'Hi, my name is {info['name']} and i live in {info['city']}
```

### 활용 3 - 정렬 가능
- 오른쪽 정렬, 왼쪽 정렬 등
```python
msg = 'hello'
print(f'{msg:>10}')
```
-> out: '~~~~~hello'(공백을 물결로 대체)
```python
print(f'{msg:<10}')
```
-> out: 'hello~~~~~'


### 활용 4 - if/else문 적용 가능
- 오른쪽 정렬, 왼쪽 정렬 등
```python
msg1 = 'hello'
msg2 = 'bye'
print(f'{hello if len (hello) > len(bye) else bye}')
```
-> out: 'hello'

### 활용 5 - 연산 가능
- 산술 연산

`print(f'{3 * 5}')`

### 활용 6 - 정수 출력 자리수 지정 가능
- : 뒤에 원하는 자릿수를 적는다

```python
for i in range(1,6):
  num = f'The number is {i:05}'
  print(num)
```
-> out:
```
The number is 00001
The number is 00002
The number is 00003
The number is 00004
The number is 00005
```

### 활용 7 - 소수점 출력 자리수 지정 가능
- : . + (원하는 자릿수) + f를 적는다

```python
pi = 3.14159265358979
print(f'pi is equal to {pi:.2f}')
```
-> out: pi is equal to 3.14


### 활용 8 - 긴 정수 사이 구분 기호 추가
```python
num = 4235426452346
print(f'{num:,}')
```
-> out: 4,235,426,452,346
```python
print(f'{num:_}')
```
-> out: 4_235_426_452_346
```python
print(f'{num:_}'.replace('_', ' '))
```
-> out: 4 235 426 452 346

### 활용 9 - 날짜 출력 방식 선택 가능
- datetime 날짜를 인식할 수 있음
```python
from datetime import datetime
this_year_xmas = datetime(2025,12,25)

print(f'This year\'s X-mas is on {this_year_xmas}')
```
-> out: This year's X-mas is on 2025-12-25 00:00:00
- pandas로 조절 가능

```python
print(f'This year\'s X-mas is on {this_year_xmas:%B, %d, %Y}')
```
-> out: This year's X-mas is on December 25, 2021