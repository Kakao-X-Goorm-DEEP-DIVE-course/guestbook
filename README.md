# Django Guestbook Project

## 📍 프로젝트 개요
이 프로젝트는 Django를 학습하고, 각 팀원이 방명록(Guestbook) 서비스를 구현하는 것을 목표로 합니다. 구현된 서비스는 Docker를 사용해 컨테이너화하여 배포할 수 있습니다.

## 📍 팀원별 작업 내용
각 팀원은 자신의 브랜치에서 작업한 후 프로젝트의 원격 저장소에 push합니다. 각자의 방명록 서비스 구현이 완료되면, main 브랜치에 병합할 계획입니다.

## 📍 목차
- [프로젝트 구조(예시)](#프로젝트-구조예시)
- [개발 환경 설정](#개발-환경-설정)
- [Django 방명록 서비스 실행 방법](#django-방명록-서비스-실행-방법)
- [Docker 컨테이너 실행 방법](#docker-컨테이너-실행-방법)
- [기여 가이드](#기여-가이드)

## 📍 프로젝트 구조(예시)
```plaintext
project-root/
│
├── guestbook/
│   ├── guestbook/  # Django 설정 파일
│   ├── entries/    # 방명록 앱
│   └── manage.py   # Django 관리 파일
│
├── Dockerfile       # Docker 이미지를 빌드하기 위한 파일
├── docker-compose.yml # Docker 컴포즈 파일
└── README.md        # 프로젝트 정보 파일
```
## 📍 개발 환경 설정
Python 3.x 버전을 설치하고 pip을 사용해 Django를 설치합니다. [설치 자료](https://freehoon.tistory.com/135)
```bash
pip install django
```
## 📍 Django 방명록 서비스 실행 방법
1. 마이그레이션 수행
```bash
python manage.py migrate
```
2. 개발 서버 실행
```bash
python manage.py runserver
```
3. 서비스 접속
브라우저에서 http://localhost:8000으로 접속합니다.
## 📍 Docker 컨테이너 실행 방법
1. Docker 이미지 빌드
```bash
docker build -t guestbook .
```
2. Docker 컨테이너 실행
```bash
docker run -p 8000:8000 guestbook
```
3. Docker Compose 사용 
```bash
docker-compose up
```
## 📍기여 가이드
1. 커밋 메시지 가이드라인
- 명확한 커밋 메시지를 사용합니다.
```plaintext
[feat] 방명록 작성 기능 추가
[fix] 방명록 오류 수정
```
2. Pull Request
- 작업이 완료되면 main 브랜치로의 Pull Request를 생성합니다.
- 리뷰를 통해 코드 품질을 개선합니다.

