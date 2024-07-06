# 베이스 이미지 설정
FROM alpine:3.18

# Node.js 설치를 위한 필수 패키지 설치
RUN apk add --no-cache \
  nodejs \
  npm
# 작업 디렉토리 설정
WORKDIR /usr/src/app

RUN npm init -y
# 애플리케이션 종속성 설치
COPY package*.json ./
RUN npm cache clean --force && npm install --save-dev


RUN npm install
RUN npm install @rollup/rollup-linux-x64-musl
RUN npm install vite vite-plugin-vuetify vuetify @vitejs/plugin-vue vue-router

# 애플리케이션 소스 복사
COPY . .

# 애플리케이션 실행
EXPOSE 5173
CMD ["npm", "run", "dev"]
