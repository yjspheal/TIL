- [Python Typing Module](#python-typing-module)
  - [Type Hints 소개](#type-hints-소개)
    - [Type Hints란?](#type-hints란)
    - [Type Hints의 장점](#type-hints의-장점)
  - [기본적인 자료형 명시](#기본적인-자료형-명시)
    - [변수](#변수)
    - [함수](#함수)
  - [typing 모듈 활용](#typing-모듈-활용)
    - [List, Tuple, Dict, Set](#list-tuple-dict-set)
    - [Union, Optional](#union-optional)
    - [Any](#any)
    - [Callable](#callable)
    - [Type Aliases](#type-aliases)

# Python Typing Module

## Type Hints 소개

### Type Hints란?

- Python 3.5부터 도입된 기능으로, 변수나 함수의 인자, 반환 값의 자료형을 명시하는 기능
- 코드의 가독성을 높이고, 잠재적인 오류를 사전에 방지할 수 있도록 도와줌
- C나 Java와 같은 정적 타입 언어처럼 강제성을 가지지는 않으며, 실행 시점에 타입 오류를 발생시키지 않음 (linter나 type checker를 통해 검사)

### Type Hints의 장점

- **가독성 향상**
  - 함수의 시그니처만 봐도 어떤 타입의 인자를 받고 어떤 타입의 값을 반환하는지 명확하게 알 수 있음
- **버그 예방**
  - 타입 체커(Mypy 등)를 사용하여 코드 실행 전에 타입 관련 오류를 발견 가능
- **개발 도구 지원**
  - IDE에서 더 정확한 코드 자동 완성, 오류 강조 등의 기능을 제공받음

## 기본적인 자료형 명시

### 변수

- 변수 이름 뒤에 콜론(`:`)을 붙이고 자료형을 명시함

```python
name: str = "Alice"
age: int = 30
is_student: bool = True
scores: list = [100, 90, 85]
```

### 함수

- 함수의 인자는 변수와 동일한 방식으로 명시함
- 반환 값은 함수 선언부의 끝에 `->` 기호를 사용해 명시함
- 반환 값이 없는 함수는 `-> None`으로 명시함

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def print_message(message: str) -> None:
    print(message)
```

## typing 모듈 활용

- 더 복잡하고 구체적인 타입을 명시하기 위해 `typing` 모듈을 사용함

### List, Tuple, Dict, Set

- 컬렉션 내부의 요소 타입을 명시 가능

```python
from typing import List, Tuple, Dict, Set

numbers: List[int] = [1, 2, 3]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"math": 90, "science": 85}
unique_numbers: Set[int] = {1, 2, 3}
```

### Union, Optional

- `Union[type1, type2, ...]`: 여러 타입 중 하나가 될 수 있음을 명시함
- `Optional[type]`: 특정 타입 또는 `None`이 될 수 있음을 명시함 `Union[type, None]`과 동일

```python
from typing import Union, Optional

def get_item(key: Union[str, int]) -> Optional[str]:
    # ...
    if key in data:
        return data[key]
    return None
```

### Any

- `Any`: 모든 타입을 허용하며, 타입 체커가 해당 부분은 검사하지 않도록 함
- 동적 타입의 특성이 필요할 때 제한적으로 사용하는 것이 좋음

```python
from typing import Any

def process_data(data: Any) -> None:
    print(data)
```

### Callable

- `Callable[[arg_type1, arg_type2], return_type]`: 함수나 메서드와 같이 호출 가능한 객체의 타입을 명시함

```python
from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(a: int, b: int) -> int:
    return a + b

result = apply_function(add, 5, 3) # 8
```

### Type Aliases

- 복잡한 타입 어노테이션을 별칭으로 만들어 재사용 가능

```python
from typing import List, Dict

Vector = List[float]
ConnectionOptions = Dict[str, str]

def create_vector() -> Vector:
    return [1.0, 2.0, 3.0]

def connect(options: ConnectionOptions) -> None:
    # ...
    pass
```
