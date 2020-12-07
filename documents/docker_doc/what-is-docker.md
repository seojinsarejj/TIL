# What is Docker?

![docker-logo](../../images/docker-logo.png "docker-logo")

## **컨테이너 기반의 오픈소스 가상화 플랫폼**

- 다양한 프로그램, 실행환경을 컨테이너로 추상화하고 동일한 인터페이스를 제공하여 프로그램의 배포 및 관리를 단순하게 해줍니다.

### 컨테이너(Container)
- 격리된 공간에서 프로세스가 동작하는 기술
- 가상화 기술 중 하나

### 이미지(Image)
- 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것
- 컨테이너 == 이미지를 실행한 상태


## Docker 작동 방식
![vm-vs-docker](../../images/vm-vs-docker.png "vm-vs-docker")

하드웨어를 가상화하는 VM과 달리 Docker는 프로세스를 격리하는 방식을 사용