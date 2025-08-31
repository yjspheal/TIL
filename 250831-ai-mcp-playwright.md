- [AI 에이전트와 MCP (Model-Controller-Parser)](#ai-에이전트와-mcp-model-controller-parser)
  - [개념](#개념)
  - [동작 과정](#동작-과정)
- [Playwright (플레이라이트)](#playwright-플레이라이트)
  - [개념](#개념-1)
  - [주요 특징](#주요-특징)
  - [간단한 Python 예시](#간단한-python-예시)
- [정리](#정리)

---

## AI 에이전트와 MCP (Model-Controller-Parser)

### 개념
- **MCP**는 AI 에이전트가 사용자의 요청을 이해하고, 적절한 도구를 선택하여 실행한 뒤, 그 결과를 다시 사용자에게 유용한 형태로 가공해 전달하는 일련의 과정을 구조화한 아키텍처 패턴입니다.
- 단순히 정보를 생성하는 것을 넘어, AI가 **실용적인 작업(Practical Action)**을 수행할 수 있게 만드는 핵심적인 방법론입니다.

### 동작 과정
1.  **Model (모델):**
    -   사용자의 프롬프트(요청)를 **이해하고 분석**하는 단계입니다.
    -   LLM(거대 언어 모델)이 사용자의 **의도를 파악**하고, 어떤 작업을 수행해야 할지, 어떤 정보가 필요한지를 결정합니다.

2.  **Controller (컨트롤러):**
    -   모델의 결정을 바탕으로 **실제 사용할 도구를 선택**하는 단계입니다.
    -   예를 들어, "파일 목록 보여줘" 라는 요청에는 `list_directory` 도구를, "웹사이트 내용 요약해줘" 라는 요청에는 `web_fetch` 도구를 선택합니다.
    -   선택된 도구에 **필요한 인자(arguments)를 전달**하여 실행을 명령합니다.

3.  **Parser (파서):**
    -   도구가 실행된 후 **반환된 결과(출력)를 해석**하는 단계입니다.
    -   API 응답, 파일 내용, 커맨드 실행 결과 등 기계가 읽기 좋은(machine-readable) 데이터를 **사람이 이해하기 쉬운(human-readable) 형태로 가공**합니다.
    -   이 가공된 정보를 바탕으로 사용자에게 보여줄 최종 응답을 생성합니다.

---

## Playwright (플레이라이트)

### 개념
- **Playwright**는 Microsoft에서 개발한 최신 **브라우저 자동화(Browser Automation)** 라이브러리입니다.
- 코드를 통해 웹 브라우저(Chrome, Firefox, Safari 등)를 제어하여, 사람이 직접 하는 것과 같은 작업을 자동으로 수행하게 할 수 있습니다.
- 주로 **웹 애플리케이션 테스트**, **웹 스크래핑(데이터 수집)** 등의 목적으로 널리 사용됩니다.

### 주요 특징
- **크로스 브라우저 지원**: 단일 API로 Chromium (Chrome, Edge), Firefox, WebKit (Safari)을 모두 제어할 수 있습니다.
- **다양한 언어 지원**: Python, JavaScript/TypeScript, Java, .NET 등 여러 인기 있는 프로그래밍 언어를 지원합니다.
- **강력한 자동 대기(Auto-wait)**: 페이지 요소가 나타나거나 상호작용 가능해질 때까지 자동으로 기다려주므로, 불안정한 테스트 코드를 크게 줄여줍니다.
- **네트워크 제어**: 네트워크 요청을 가로채거나 수정하는 등 고급 기능을 제공하여 테스트 환경을 완벽하게 제어할 수 있습니다.

### 간단한 Python 예시
'''python
# Playwright 라이브러리 설치 필요
# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright

def run(playwright):
    # 브라우저 실행 (headless=False로 하면 브라우저 창이 실제로 보임)
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # 'https://www.google.com'으로 이동
    page.goto("https://www.google.com")

    # 페이지 제목 출력
    print(f"페이지 제목: {page.title()}")

    # 입력창에 'Playwright' 입력
    page.get_by_role("combobox", name="검색").fill("Playwright")

    # 'Google 검색' 버튼 클릭
    page.get_by_role("button", name="Google 검색").first.click()

    # 결과 페이지의 스크린샷 저장
    page.screenshot(path="playwright_search_result.png")
    print("스크린샷을 'playwright_search_result.png' 파일로 저장했습니다.")

    # 브라우저 종료
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
'''

---

## 정리
- **MCP**는 AI가 **생각(Model)**하고, **행동(Controller)**하며, **결과를 해석(Parser)**하는 체계적인 방법을 제공합니다.
- **Playwright**는 이러한 '행동'의 한 예시로, 웹 브라우저를 제어하는 강력하고 실용적인 도구입니다.
- 두 개념의 조합을 통해 AI는 사용자를 대신하여 웹사이트에서 정보를 찾아오거나, 특정 작업을 자동으로 수행하는 등 고차원적인 서비스를 제공할 수 있게 됩니다.
