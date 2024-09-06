From python:3.8.10 AS builder

#컨테이너 내부에서 파이썬이 입출력을 버퍼에 담아 쏘는데, 그러지 말고 로그를 실시간으로 출력
ENV PYTHONUNBUFFERED 1

#디렉터리 생성
RUN mkdir /code

#작업 포인터 지정
WORKDIR /code

#의존성 갖고와서
ADD requirements.txt /code/

#설치
RUN pip install --user --no-cache-dir -r requirements.txt

#--------------------------------#
From python:3.8.10-slim AS runner

ENV PYTHONUNBUFFERED 1

WORKDIR /code

#설치된 프로그램 복사
COPY --from=builder /root/.local /root/.local

ADD . /code/

ENV PATH=/root/.local/bin:$PATH