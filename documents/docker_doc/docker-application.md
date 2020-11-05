
# 컨테이너 애플리케이션 구축

- 대부분의 서비스는 여러 에이전트나 데이터베이스 등과 연결되어 완전한 서비스로써 동작하는 것이 일반적이다.
- 여러 애플리케이션을 한 컨테이너에 설치할 수도 있지만 각 애플리케이션을 하나의 컨테이너에서 동작시키면 독립성 보장, 버전 관리, 소스코드 모듈화 등이 더욱 쉬워진다.


```bash
docker run -d \
--name wordpressdb \
-e MYSQL_ROOT_PASSWORD=password \
-e MYSQL_DATABASE=wordpress \
mysql:5.7
```

```bash
docker run -d \
-e WORDPRESS_DB_PASSWORD=password \
--name wordpress \
--link wordpressdb:mysql \
-p 80 \
wordpress
```

- 데이터베이스와 워드프레스 웹 서버 컨테이너를 연동한다.


`localhost:32769`로 접속하여 확인합니다.