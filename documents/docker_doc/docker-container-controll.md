# 도커 컨테이너 다루기

## 컨테이너 생성

### 도커 엔진의 버전을 확인한다.
```bash
docker -v
```


### 컨테이너를 생성한다. 
`docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
- **docker run** : 컨테이너를 생성하고 실행
- **create** : 컨테이너 생성 ( 내부 접속 X )
- **start** : 컨테이너 실행
- **attach** : 컨테이너 내부로 들어감

```bash

docker run -i -t ubuntu:14.04

docker create -i -t --name mycentos centos:7

docker start mycentos

docker attach mycentos
```



#### 옵션


| 옵션 | 의미 |
---| :---: | ---:
-d | detached mode 흔히 말하는 백그라운드 모드 |
-p | 호스트와 컨테이너의 포트를 연결 (포워딩) |
-v | 호스트와 컨테이너의 디렉토리를 연결 (마운트) |
-e | 컨테이너 내에서 사용할 환경변수 설정 |
--name | 컨테이너 이름 설정 |
--rm | 프로세스 종료시 컨테이너 자동 제거 |
-it | -i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 |
--network | 네트워크 연결 |


### 컨테이너를 정지한다.
```bash
exit
```
- exit : 컨테이너를 정지한 후 빠져나온다.
- Ctrl + P,Q : 컨테이너를 정지하지 않고 빠져나온다.


### 이미지를 내려받는다.
```bash
docker pull centos:7
```


## 컨테이너 목록 확인

```bash
docker ps
```
- 지금까지 생성한 컨테이너의 목록을 확인한다.
- 정지되지 않은 컨테이너만 출력한다.

```bash
docker ps -a
```
- 정지된 컨테이너를 포함한 모든 컨테이너를 출력한다.

### command

- 컨테이너가 시작될 떄 실행될 명령어
- 이미지에 내장된 커맨드는 docker run이나 create 명령어의 맨 끝에 입력해서 컨테이너를 생성할 떄 덮어쓸 수 있다.

```bash
docker run -i -t ubuntu:14.04 echo hello world!
```

- 위 명령어로 생성된 컨테이너는 ubuntu:14.04 이미지에 내장된 커맨드인 /bin/bash를 덮어쓰기 때문에 상호입출력이 가능한 셸이 실행되지 않는다.
- 'hello world!'만 출력되고 컨테이너가 종료된다.

### rename

```bash
docker rename angry_morse my_container
```
- rename을 사용하여 컨테이너의 이름을 변경할 수 있습니다.


## 컨테이너 삭제

다음 명령어를 사용해 컨테이너를 삭제한다.

```bash
docker rm angry_morse
```

- 실행 중인 컨테이너는 삭제할 수 없다.
- 다음은 실행 중인 컨테이너를 삭제하는 옵션이다.

```bash
docker rm -f mycentos
```

### prune 
- 모든 컨테이너를 삭제할 수 있다. 
```bash
docker container prune
```

또는 다음과 같이 사용할 수 있다.

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

