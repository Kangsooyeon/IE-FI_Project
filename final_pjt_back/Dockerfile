# Python 3.9 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python manage.py loaddata fixtures/depositproducts.json

RUN python manage.py loaddata fixtures/savingproducts.json

RUN python manage.py loaddata fixtures/depositoptions.json

RUN python manage.py loaddata fixtures/savingoptions.json

RUN python manage.py loaddata fixtures/exchangerate.json

RUN python manage.py loaddata fixtures/countryflag.json

RUN python manage.py loaddata fixtures/location.json

RUN python manage.py loaddata fixtures/user.json

RUN python manage.py loaddata fixtures/article.json

RUN python manage.py loaddata fixtures/comment.json

RUN python manage.py loaddata fixtures/subscribeddepositproducts.json

RUN python manage.py loaddata fixtures/subscribedsavingproducts.json

# RUN chmod +x /app/init.sh
# RUN /bin/sh /app/init.sh


# 포트 설정
EXPOSE 8000

# 명령어 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]