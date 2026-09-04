# TIL Repository Agent Rules

## Language

- 사용자 안내, 작업 메모, 새 TIL 본문은 한국어로 작성한다.

## Repository structure

- 저장소 최상위 학습 분야 디렉터리: `Python/`, `SQL/`, `Algorithm/`, `Web/`, `AI/`, `InformationProcessingEngineer/`
- 기존 학습 파일은 주제에 맞는 최상위 디렉터리로 관리한다. 파일명과 내용은 변경하지 않는다
- 정보처리기사 학습 자료만 `InformationProcessingEngineer/` 아래에 작성한다
- 정보처리기사 하위 디렉터리: `SQL/`, `Programming/`, `Database/`, `SoftwareEngineering/`, `Network/`, `Security/`, `ErrorNote/`
- 기존 SQL 학습 기록은 `SQL/`에 보존하며 `InformationProcessingEngineer/SQL/`로 옮기지 않는다
- 새 정보처리기사 TIL은 주제에 맞는 하위 디렉터리에만 추가한다. 불필요한 파일이나 디렉터리를 만들지 않는다

## Existing TIL preservation

- 기존 TIL 파일은 삭제, 이름 변경, 내용 변경을 하지 않는다
- 구조 개편에서 허용되는 기존 TIL 변경은 주제별 디렉터리로의 이동뿐이다

## New TIL format

- 파일명은 기본적으로 `YYMMDD-topic.md` 형식을 사용한다
- 최상위 제목(`#`)으로 주제를 표시하고, `##` 이하 제목으로 내용을 구조화한다
- 설명은 `-` 목록 중심으로 간결하게 작성한다
- 코드·문법 예시는 언어를 명시한 코드 블록을 사용한다
- 문장은 명사형 또는 `-다`로 간결하게 끝낸다. 존댓말, `~습니다`체, 설명문 끝의 마침표는 사용하지 않는다
- 정의·대조가 필요하면 콜론(`:`)과 하위 목록을 우선 사용한다
- 기존 파일명 규칙과 Markdown 문체를 최대한 유지한다

## README

- 기존 `README.md`의 내용과 형식을 보존한다
- 파일 이동 후 기존 TIL 링크를 새 경로로 갱신한다
- 정보처리기사 학습 영역을 소개할 필요가 있을 때만 기존 문체에 맞는 섹션을 추가한다
- 해당 섹션에는 `SQL`, `Programming`, `Database`, `Software Engineering`, `Network`, `Security`, `Error Note` 하위 디렉터리 링크를 포함한다

## Git and verification

- 커밋 메시지는 `action filename` 형식을 사용한다. 예: `update README.md`, `create 260907-select.md`
- 여러 파일을 커밋할 때 TIL 파일이 있으면 해당 TIL 파일명을 우선한다. TIL 파일이 여러 개면 `update TILs`를 사용한다
- 작업 전후 `git diff`와 `git status`를 확인한다
- 기존 학습 기록의 파일명과 내용이 변경되지 않았는지 반드시 검증한다
