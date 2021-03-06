# Context Switching

> 멀티 프로세스 환경에서 CPU가 어떤 하나의 프로세스를 실행하고 있는 상태에서 인터럽트 요청에 의해 다음 우선 순위의 프로세스가 실행되어야 할 떄 기존의 프로세스 상태 또는 레지스터 값을 저장하고 CPU가 다음 프로세스를 수행하도록 새로운 프로세스의 상태 또는 레지스터 값을 교체하는 작업

![context-switching](../../images/context-switching.png "context-switching")

## Context

> 사용자와 다른 사용자, 사용자와 시스템 또는 디바이스간의 상호작용에 영향을 미치는 사람, 장소, 개체등의 현재 상황(상태)을 규정하는 정보

- OS에서는 CPU가 해당 프로세스를 실행하기 위한 해당 프로세스의 정보들을 말함 (레지스터 값)
- Context는 프로세스의 PCB(Process Control Block)에 저장됨
- PCB의 저장 정보
  - 프로세스의 상태 : 생성,준비,수행,대기,중지
  - 프로그램 카운터 : 프로세스가 다음에 실행할 명령어 주소
  - 레지스터 : 누산기,스택,색인 레지스터
  - 프로세스 번호
- Context Switching떄 해당 CPU는 아무런 일을 하지 못한다. 따라서 잦은 컨텍스트 스위칭은 오버헤드를 발생시킨다.

## Interrupt

- 1. I/O interrupt
- 2. CPU 사용시간 만료
- 3. 자식 프로세스 Fork

-> OS 스케쥴러가 스위칭을 실행함

## Process vs Thread

- 스레드의 경우 stack을 제외한 나머지 영역(Code,Data,Heap)은 부모 프로세스의 영역을 공유하기 때문에 PCB에는 stack 및 간단한 정보만 저장하게 된다. 따라서 프로세스보다 컨텍스트 스위칭이 더 빠르다
