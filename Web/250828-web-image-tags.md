- [HTML의 `<img>`와 CSS의 `background-image` 차이](#html의-img와-css의-background-image-차이)
  - [1. `<img>` 태그](#1-img-태그)
  - [2. `background-image` (CSS)](#2-background-image-css)
  - [비교 요약](#비교-요약)

---

## HTML의 `<img>`와 CSS의 `background-image` 차이

### 1. `<img>` 태그
- HTML 문서의 **콘텐츠 요소**로서 이미지 삽입
- 문서 구조상 의미 있는 데이터로 취급됨 (시맨틱 요소)
- **대체 텍스트(alt)** 제공 가능 → 접근성/SEO에 중요
- 이미지 자체가 레이아웃의 일부로 인식됨

예시:
```html
<img src="cat.png" alt="고양이 사진">
```

### 2. `background-image` (CSS)
- HTML 요소의 **스타일/디자인 목적**으로 배경에 이미지 삽입
- 문서 콘텐츠와는 별개, 꾸밈(장식) 용도
- alt 속성 제공 불가 → 스크린리더/SEO에 영향 없음
- 반복, 크기 조정, 위치 제어 등 스타일 속성과 함께 사용 가능

예시:
```css
div {
  background-image: url("cat.png");
  background-size: cover;
  background-repeat: no-repeat;
}
```

### 비교 요약

| 구분                  | `<img>` 태그                              | `background-image` (CSS)                     |
|-----------------------|-------------------------------------------|---------------------------------------------|
| 역할                  | 문서의 콘텐츠(데이터)                    | 스타일(디자인)                              |
| 의미/시맨틱           | 있음 (SEO, 접근성에 중요)                 | 없음 (순수 시각적 효과)                      |
| 대체 텍스트 가능 여부 | 가능 (`alt`)                              | 불가능                                      |
| 조작 방법             | HTML 속성으로 삽입                        | CSS 속성으로 삽입                            |
| 용도                  | 콘텐츠 전달 (예: 기사 이미지, 상품 사진)  | 디자인 장식 (예: 배경 패턴, 꾸밈 요소)       |

---