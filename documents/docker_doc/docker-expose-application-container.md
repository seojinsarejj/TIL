# 컨테이너를 외부에 노출

- 컨테이너는 가상 머신과 마찬가지로 가상 IP 주소를 할당한다.
- ipconfig로 확인 가능한다.
- 애플리케이션을 노출하기 위해서는 eth0의 IP와 포트를 호스트의 IP와 포트에 바인딩해야 한다.


```bash
docker run -i -t --name mywebserver -p 80:80 ubuntu:14.04
```
- -p 옵션은 컨테이너의 포트를 호스트의 포트와 바인딩해 연결할 수 있게 설정한다.


```bash
docker run -i -t -p 3306:3306 -p 192.168.0.100:7777:80 ubuntu:14.04
```
- 호스트의 특정 IP를 컨테이너의 80번 포트와 연결한다.
- 여러 개의 포트를 외부에 개방하려면 -p 옵션을 여러 번 써서 설정한다.

```bash
apt-get update
apt-get install apache2 -y
service apache2 start
```

- 다음 명령어를 차례로 입력해 아파치 웹 서버를 설치한다.

`호스트 IP의 80번 포트로 접근 -> 80번 포트는 컨테이너의 80번 포트로 포워딩 -> 웹 서버 접근`


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