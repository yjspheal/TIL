- [부트스트랩 (Bootstrap) 이란?](#부트스트랩-bootstrap-이란)
- [핵심 특징](#핵심-특징)
  - [1. 반응형 그리드 시스템 (Grid System)](#1-반응형-그리드-시스템-grid-system)
  - [2. 미리 디자인된 컴포넌트 (Components)](#2-미리-디자인된-컴포넌트-components)
  - [3. 유틸리티 클래스 (Utilities)](#3-유틸리티-클래스-utilities)
- [사용 방법](#사용-방법)
  - [CDN을 이용한 방법](#cdn을-이용한-방법)
- [장점](#장점)

---

## 부트스트랩 (Bootstrap) 이란?

- 트위터에서 시작된 오픈소스 프론트엔드 프레임워크.
- 반응형(Responsive), 모바일 우선(Mobile-first) 웹사이트를 쉽고 빠르게 개발할 수 있도록 도와주는 HTML, CSS, JavaScript 템플릿과 도구들의 모음이다.

---

## 핵심 특징

### 1. 반응형 그리드 시스템 (Grid System)
- 부트스트랩의 가장 강력한 기능으로, 화면 크기에 따라 웹페이지의 레이아웃을 자동으로 조정해준다.
- 전체 너비를 12개의 열(column)으로 나누고, 이 열들을 조합하여 요소를 배치한다.
- `.container`, `.row`, `.col-*` 등의 클래스를 사용하여 구조를 만든다.

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">화면이 중간 크기 이상일 때 50% 너비</div>
    <div class="col-md-6">화면이 중간 크기 이상일 때 50% 너비</div>
  </div>
</div>
```

### 2. 미리 디자인된 컴포넌트 (Components)
- 네비게이션 바, 버튼, 카드, 모달, 캐러셀(이미지 슬라이더) 등 웹사이트에서 자주 사용되는 UI 요소들이 미리 디자인되어 클래스 이름만으로 쉽게 가져다 쓸 수 있다.
- 이를 통해 개발자는 디자인에 드는 시간을 크게 줄이고 기능 개발에 집중할 수 있다.

```html
<!-- 예시: 기본 버튼과 Primary 버튼 -->
<button type="button" class="btn">Basic</button>
<button type="button" class="btn btn-primary">Primary</button>
```

### 3. 유틸리티 클래스 (Utilities)
- 정렬, 여백(margin/padding), 색상, 테두리 등 세부적인 스타일을 CSS 파일을 직접 수정하지 않고 HTML 클래스만으로 적용할 수 있게 해준다.
- `mt-3` (margin-top), `p-5` (padding), `text-center` (가운데 정렬), `bg-dark` (어두운 배경) 등이 있다.

```html
<div class="text-center mt-5 p-3 bg-light">
  이 div는 위쪽 여백이 있고, 안쪽 여백이 있으며, 텍스트가 가운데 정렬되고, 밝은 회색 배경을 가집니다.
</div>
```

---

## 사용 방법

### CDN을 이용한 방법
- 가장 간단한 방법으로, HTML 파일에 CDN(Content Delivery Network) 링크를 추가하기만 하면 된다. 별도의 설치 과정이 필요 없다.

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap CDN 예제</title>
    <!-- Bootstrap CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <h1>안녕하세요, 부트스트랩!</h1>
    <!-- Bootstrap JS CDN (컴포넌트 동작에 필요) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

---

## 장점
- **개발 속도 향상**: 미리 만들어진 요소들을 활용하여 프로토타입이나 실제 웹사이트를 매우 빠르게 만들 수 있다.
- **반응형 웹 지원**: 그리드 시스템을 통해 모바일, 태블릿, 데스크탑 등 다양한 기기에 맞는 레이아웃을 쉽게 구현할 수 있다.
- **디자인 일관성**: 정해진 디자인 시스템을 따르므로 전체 웹사이트의 디자인 톤앤매너를 일관되게 유지할 수 있다.
- **방대한 커뮤니티와 문서**: 사용자가 많아 관련 자료나 예제를 찾기 쉽고, 공식 문서가 매우 잘 되어 있다.
