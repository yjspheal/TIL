# LangChain

- [LangChain이란](#langchain이란)
- [LangChain의 주요 구성 요소](#langchain의-주요-구성-요소)
  - [LLM (Large Language Models)](#llm-large-language-models)
  - [Prompt Templates](#prompt-templates)
  - [Output Parsers](#output-parsers)
  - [Chains](#chains)
- [기본 활용법 및 코드 예시](#기본-활용법-및-코드-예시)

---

## LangChain이란

- LLM을 기반으로 하는 애플리케이션을 쉽게 개발할 수 있도록 도와주는 프레임워크

## LangChain의 주요 구성 요소

### LLM (Large Language Models)

- LangChain의 핵심으로, 다양한 언어 모델과 상호작용하는 인터페이스를 제공

### Prompt Templates

- 사용자 입력을 받아 동적으로 프롬프트를 생성하는 템플릿
- 재사용성과 일관성을 높여줌

### Output Parsers

- LLM의 출력을 원하는 형식으로 변환하는 역할
- 예시
  - JSON 형식으로 변환
  - 특정 데이터만 추출

### Chains

- 여러 구성 요소를 순차적으로 연결하여 복잡한 작업을 수행하는 기능
- 가장 기본적인 `LLMChain`은 프롬프트 템플릿, LLM, 출력 파서를 연결

## 기본 활용법 및 코드 예시

- `LLMChain`을 사용하여 특정 주제에 대한 질문과 답변을 생성하는 예시

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 1. LLM 준비
# API 키 설정 필요
# llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# 2. Prompt Template 정의
prompt = PromptTemplate(
    input_variables=["topic"],
    template="{topic}에 대해 간단히 설명해줘",
)

# 3. Chain 생성
# chain = LLMChain(llm=llm, prompt=prompt)

# 4. Chain 실행
# result = chain.invoke({"topic": "인공지능"})
# print(result)
```
