# 컨테이너 목록 확인

```bash
docker ps
```
- 지금까지 생성한 컨테이너의 목록을 확인한다.
- 정지되지 않은 컨테이너만 출력한다.

```bash
docker ps -a
```
- 정지된 컨테이너를 포함한 모든 컨테이너를 출력한다.

## command

- 컨테이너가 시작될 떄 실행될 명령어
- 이미지에 내장된 커맨드는 docker run이나 create 명령어의 맨 끝에 입력해서 컨테이너를 생성할 떄 덮어쓸 수 있다.

```bash
docker run -i -t ubuntu:14.04 echo hello world!
```

- 위 명령어로 생성된 컨테이너는 ubuntu:14.04 이미지에 내장된 커맨드인 /bin/bash를 덮어쓰기 때문에 상호입출력이 가능한 셸이 실행되지 않는다.
- 'hello world!'만 출력되고 컨테이너가 종료된다.

##rename

```bash
docker rename angry_morse my_container
```
- rename을 사용하여 컨테이너의 이름을 변경할 수 있습니다.