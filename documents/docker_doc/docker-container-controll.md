# 도커 컨테이너 다루기

## 컨테이너 생성

### 도커 엔진의 버전을 확인한다.
```bash
docker -v
```


### 컨테이너를 생성한다. (run)
- docker run : 컨테이너를 생성하고 실행하는 역할
- -i -t : 컨테이너와 상호 입출력을 가능하게 하는 역할
- ubuntu:14.04 : 컨테이너를 생성하기 위한 이미지의 이름
```bash
docker run -i -t ubuntu:14.04
```

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

### 컨테이너를 생성한다. (create)
- create : 컨테이너 생성 ( 내부 접속 X )
- start : 컨테이너 실행
- attach : 컨테이너 내부로 들어감

```bash
docker create -i -t --name mycentos centos:7

docker start mycentos

docker attach mycentos
```






