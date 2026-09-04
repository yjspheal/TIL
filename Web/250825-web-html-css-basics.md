- [웹의 기본 구성 요소](#웹의-기본-구성-요소)
- [HTML (HyperText Markup Language)](#html-hypertext-markup-language)
  - [역할과 개념](#역할과-개념)
  - [기본 구조](#기본-구조)
  - [주요 태그 예시](#주요-태그-예시)
- [CSS (Cascading Style Sheets)](#css-cascading-style-sheets)
  - [역할과 개념](#역할과-개념-1)
  - [기본 문법](#기본-문법)
  - [HTML에 CSS 적용하기](#html에-css-적용하기)

---

## 웹의 기본 구성 요소

웹 페이지는 크게 세 가지 요소로 구성된다.

1.  **HTML**: 웹 페이지의 **구조와 내용**을 담당한다. (뼈대)
2.  **CSS**: 웹 페이지의 **디자인과 스타일**을 담당한다. (옷, 꾸미기)
3.  **JavaScript**: 웹 페이지의 **동적인 기능과 상호작용**을 담당한다. (움직임, 동작)

---

## HTML (HyperText Markup Language)

### 역할과 개념
- 웹 페이지의 뼈대를 만드는 표준 마크업 언어.
- **태그(Tag)**들을 사용하여 웹 페이지의 제목, 문단, 이미지, 링크 등 다양한 요소의 구조와 의미를 정의한다.
- **요소(Element)**는 시작 태그, 내용, 종료 태그로 구성된다. (예: `<p>이것은 문단입니다.</p>`)
- **속성(Attribute)**은 요소에 추가적인 정보를 제공한다. (예: `<a href="https://www.google.com">구글 링크</a>`에서 `href`는 속성)

### 기본 구조
```html
<!DOCTYPE html> <!-- 이 문서가 HTML5 문서임을 선언 -->
<html>
  <head>
    <!-- 문서의 메타데이터(설정 정보)를 담는 부분 -->
    <meta charset="utf-8"> <!-- 문자 인코딩 설정 -->
    <title>페이지 제목</title>
  </head>
  <body>
    <!-- 사용자에게 실제로 보여지는 모든 콘텐츠를 담는 부분 -->
    <h1>가장 큰 제목</h1>
    <p>이것은 문단입니다.</p>
    <a href="#">이것은 링크입니다.</a>
  </body>
</html>
```

### 주요 태그 예시
- `<h1>`, `<h2>`, ... `<h6>`: 제목 태그
- `<p>`: 문단 (paragraph)
- `<a>`: 하이퍼링크 (anchor)
- `<img>`: 이미지
- `<div>`: 특별한 의미 없이 구역을 나눌 때 사용 (division)
- `<span>`: 특별한 의미 없이 텍스트의 일부를 묶을 때 사용

---

## CSS (Cascading Style Sheets)

### 역할과 개념
- HTML로 만들어진 문서의 **시각적 표현(스타일)**을 꾸미는 언어.
- 색상, 글꼴, 여백, 레이아웃 등 웹 페이지의 디자인을 담당한다.

### 기본 문법
- **선택자(Selector)**와 **선언 블록(Declaration Block)**으로 구성된다.
- 선언 블록은 `{}` 안에 `속성(property): 값(value);` 형태로 작성한다.

```css
/* p 태그를 선택자로 사용 */
p {
  color: blue; /* 글자 색상을 파란색으로 */
  font-size: 16px; /* 글자 크기를 16픽셀로 */
}

/* .important 클래스를 선택자로 사용 */
.important {
  font-weight: bold;
}

/* #main-title 아이디를 선택자로 사용 */
#main-title {
  border-bottom: 1px solid black;
}
```

### HTML에 CSS 적용하기
1.  **인라인 스타일(Inline Style)**: HTML 태그에 `style` 속성을 직접 추가. (권장되지 않음)
    `<p style="color: red;">빨간색 텍스트</p>`
2.  **내부 스타일 시트(Internal Style Sheet)**: HTML 문서의 `<head>` 안에 `<style>` 태그를 사용.
3.  **외부 스타일 시트(External Style Sheet)**: 별도의 `.css` 파일을 만들어 HTML 문서의 `<head>`에서 `<link>` 태그로 연결. (가장 권장되는 방법)
    `<link rel="stylesheet" href="styles.css">`
