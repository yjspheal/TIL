# 교육자료 링크

[14기_0716_SW_AI 스타트캠프_파이썬트랙_Day1](https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2025071517534781300/index.html)

- 48p~

[14기_0717_SW_AI 스타트캠프_파이썬트랙_Day2](https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2025071517550529300/index.html)

# Git

- 분산 버전 관리 시스템

## 버전 관리란?

- **변화를 기록하고 추적**하는 것이 핵심
    - v3.1에서 v4.0이 올 때 무엇이 바뀌었는가-
- 돌아가고 싶을 때는 변화된 것만 없애주면 됨
- 또한 자료의 양이 많아질 때,
    - 예를 들어 v1이 1000줄, v2가 1200줄, v3가 1300줄이라면
    - v1 - 1000, v2 - 200, v3 - 100줄만 기록하면 되므로 기하급수적으로 분량이 늘어나지 않음
- 마지막 파일과 이전 변경사항만 남기는 것!

![image.png](attachment:ffa2a85f-e217-4f37-b61f-fe08865af45b:image.png)

## 중앙  vs 분산

### 중앙 집중식

- 버전이 중앙 서버에 저장되고, 중앙 서버에서 파일을 가져와 다시 중앙에 업로드

### 분산식

- 버전을 여러 개의 복제된 저장소에 저장 및 관리

### 분산식의 장점

- 중앙 서버에 의존하지 않고 도시에 다양한 작업 수행 가능
    - 즉 개발자간 작업 충돌을 줄여주고 생산성이 향상됨
        - 물론 아예 안 나는 건 아님. 근데 해결과젇ㅇ이 훨씬 쉬울뿐
- 중앙이 터져도 백업과 복구가 용이
- 인터넷에 연결되지 않아도 작업을 계속할 수 있음
    - 변경 이력을 로컬에 기록하고 나중에 중앙과 동기화

## git의 역할

- 코드의 버전(히스토리)를 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

⇒ 코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구

## git의 영역

### Working Directory(WD)

- 실제 작업 중인 파일들이 위치하는 영역. 걍 우리가 보는 폴더

### Staging Area(SA)

- 직접 눈으로 볼 수 없고, CLI로만 확인 가능
- WD에서 변경된 파일 중, 다음 버전에 포함 시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- WD는 계속 변화를 감지하고 있기 때문에, 모든 변경 사항을 다 기록할 필요는 없으므로 선택적으로 하는 것
- 반드시 거쳐야 함. 안 거치고 보내는 기능은 없음

### Repository

- 버전 이력이 영구적으로 저장되는 영역. 모든 버전과 변경 이력이 기록됨.
    - 버전 = commit
- 눈으로 못봄. CLI 으로 볼 것
- 협업 할 때 서로 잘 맞추고 공유해야 하는 것.

## commit이란?

변경된 파일들을 저장하는 행위.

사진을 찍듯이 기록한다하여 snapshot이라고 함.

## git의 동작

- 모든 명령어는 git부터 시작
- git의 단위는 각 ‘프로젝트’가 되어야 함

### `git init`

- initialize의 약자
- 로컬 저장소를 여기로 하겠다는 선언
- git의 버전 관리를 시작할 디렉토리에서 진행함
- 이거 하고나면 (master)가 생김.
    - 우리가 지금 로컬 저장소에 잇다는 뜻
        - 사실 정확히는 그 뜻이 아니지만 지금은 대충 그렇게 이해할 것

![image.png](attachment:e6d3cb03-40a9-4c4f-81e9-81453bb18ca8:image.png)

### `git add`

- ‘변경 사항이 있는 파일’을 WD → SA로 올리는 명령어
    - 꼭 파일 내의 변경 만을 뜻하는 게 아니라, 파일이 생기거나 없어지는 것도 변경사항이 됨.

```bash
git add . # 현재 디렉토리 하위영역에 있는 모든 파일을 add
```

### `git commit`

- SA에 있는 파일들을 repo에 올리는 것
    - 해당 시점의 버전을 생성하고 변경 이력을 남기는 것
- 이거 하면 SA가 비게 됨

```bash
git commit -m "first commit"
```

- -m ⇒ message
    - 즉 버전명을 만드는 것

### `git status`

- 현재 WD, SA의 상태를 보여주는 코드

![image.png](attachment:b6bd5a7d-b737-41c7-9936-f41b441a8e2a:image.png)

- 지금까지 한번도 커밋이 되지 않고 추적된 적 없는 파일이(untracked되는 파일이) 있다
- first.py를 버전으로 만들고자 한다면 `git add`를 쓰라

![image.png](attachment:52fb3fa2-f53f-409e-88a1-2797e7e089a4:image.png)

- 커밋이 되어야 하는 파일이 있다(=SA에는 올라와있다)
    - WD = 빨강, SA = 초록
- unstage하고싶으면 `git rm —cached` 저거 해라

### configuration하기

- 내가 누군지 서명을 줘야 commit을 할 수 있음
- 저기서 시키는대로 user email과 name을 주면 됨
- 컴터 하나에선 한번만 하면 됨(사용자 바뀌기 전까지)

![image.png](attachment:1c4a9e9d-0269-461a-922e-6b334a2d0c63:image.png)

```bash
git config --global -l # git global 설정 어케됐는지 보기
```

### `git log`

- 커밋 리스트를 보여주는 명령어

![image.png](attachment:94be219f-dd8b-44a9-8102-00f51bd3dd50:image.png)

- 저자가 누구고, 언제몇시에 했고, 버전명은 무엇이고를 알려줌

`git log --oneline`

- commit 목록 한 줄로 보기
바

### 바로 직전 생성한 commit 수정

```bash
git commit --amend
```

- commit 메세지 수정
    - add가 된 거 없는 상태에서 저거 치면 vim 에디터가 나옴
        - Vim 에디터
            - 수정 모드(내용을 작성하는 모드), 명령 모드(저장, 삭제, 종료 etc) 존재
                - 수정 → 명령 `i`
                - 명령 → 수정 `esc`
                - 명령은 `:` 콜론 이후에 특정 키워드를 입력하여 작성
                - `:wq` 하면  쓰기 후 나가기 ㄱㄴ
    - 잘 보면 commit 랜덤hash값이 바뀐 걸 볼 수 있음
        - 즉 커밋 자체를 갈아끼워버린 것

- commit 전체 수정(뭐 빼고 커밋했다든가..)
    - add가 된 게 있는 상태에서 저걸 치면 또 vim 나옴
        - 근데 이번엔 알아서 직전 커밋에 add된거까지 더해서 커밋 만들어줌
        - 그대로 다시 나오면 됨
    - 이렇게 하면 커밋은 한개인가 두개인가?
        - 한개. git log 찍어보면 한개 나옴

## git 주의사항

1. git 저장소 내부에 git저장소는 위치할 수 없다
    1. 그렇게 되는 순간 상위 저장소는 해당 하위 저장소를 추적할 수 없게 됨
    2. 따라서 막 뭐 바탕화면 같은 데에 git 저장소 만들지 말아야함
        1. (master)이 떠있는 곳에 init을 하면 안 됨
2. git init을 하는 순간 어떤 숨김 폴더가 생성됨.
    1. 저장소 잘못 만들었으면 그 숨겨진 폴더(.git)만 지우면 됨

# 여기서부터 다음 교재

# 원격 저장소

- 코드와 버전 관리 이력을 온라인에 올려두겠다
- 3대장 gitlab github bit어쩌구

## remote 연결

```bash
git remote add origin remote_repo_url
```

- 나 remote에 add할거야 / 이름 / 이름의 실제 주소
- 보통 첫번째 저장소의 이름(닉넴)은 origin
    - 닉넴 없으면 매번 https:.//어쩌구 해야돼서 개귀찮음
    - 

### remote 리스트 확인하기

`git remote -v`

![image.png](attachment:87210260-1d1a-4d4f-a69f-e7c79c906cbc:image.png)

- 두줄인데요?
    - 한줄인 것과 같습니다

## push

```bash
git push origin master
```

- 나 푸시할거야 , origin에 , master에 있는 커밋들을(=master라는 이름의 브랜치를)

이거 하면 로그인하라는 창이 뜸

- 왜? 나 크롬에서 로그인햇는데?
    - 깃허브 입장에서 로컬은 …..헤어지자고? 너 누군데?
    - 그럼 앞으로 레포 만들고 remote만들때마다 인증해야되나요?
        - 아님. 깃헙에서 이 컴에 ‘내(노유정) 인증서’를 줬음
    
    ![image.png](attachment:da40b678-4d0c-4506-b013-0e0234d2e797:image.png)
    
    - 저 증명서는 나중에 자리 바꿨을 때 지우면 됨

## pull

![image.png](attachment:1f794763-7af6-45e3-9640-5a231cd97f64:image.png)

![image.png](attachment:4e528302-290e-4130-89b1-22065fc2cbf3:image.png)

```bash
git pull origin master
```

- 원격 저장소의 변경사항만을 받아옴(업데이트)

## clone

- 전체 다운로드
- 새 컴에서 진행할 때 사용

```bash
git clone 그_레포의_url
```

- clone으로 받아오면 init 안 해도 됨.
    - 이미 master 찍혀있는 것을 볼 수 있
- log 찍어보면 커밋도 똑같이 가져온 걸 알 수 있음

## gitignore

- 올리지 말아야할 폴더를 저장해두는 곳
    - 사용자 정보 db
    - api key 등
- 애초에 commit이 되지 않게끔 처리

### 사용 방법

1. `.gitignore`  라는 파일 생성
2. 해당 파일에 커밋 제외하고 싶은 파일명 적어서 저장
3. 그럼 `.gitignore` 은 커밋되지만, 제외하고픈 파일은 커밋되지않음.

# github 활용

## 포트폴리오 작성

### TIL 레포 정리

[NAVER D2](https://d2.naver.com/news/3435170)

- 추가적으로 스스로 학습한 것을 기로갛는 것
    - `git rm`  이게 먼지 공부하기