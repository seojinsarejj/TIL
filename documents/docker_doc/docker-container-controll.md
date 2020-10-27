# 도커 컨테이너 다루기

## 컨테이너 생성

### 도커 엔진의 버전을 확인한다.
```bash
docker -v
```


### 컨테이너를 생성한다.
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

### 이미지를 내려받는다.
```bash
docker pull centos:7
```

