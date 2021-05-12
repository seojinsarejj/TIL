# 3 way handshake

> TCP 통신을 이용하여 데이터를 전송하기 위해 네트워크 연결을 설정(Connection Establish) 하는 과정

![3-way-handshake](../../images/3-way-handshake.png "3-way-handshake")

### [STEP 1]

- A 클라이언트는 B 서버에 접속을 요청하는 SYN 패킷을 보낸다.
- 이떄 A 클라이언트는 SYN을 보내고 SYN/ACK 응답을 기다리는 **SYN_SENT** 상태, B 서버는 **Wait for Client** 상태이다.

### [STEP 2]

- B 서버는 SYN 요청을 받고 A 클라이언트에게 요청을 수락한다는 ACK와 SYN flag 가 설정된 패킷을 발송하고 A가 다시 ACK으로 응답하기를 기다린다. 이때 B 서버는 SYN_RECEIVED 상태가 된다.

### [STEP 3]

- A 클라이언트는 B 서버에게 ACK을 보내고 이후로부터는 연결이 이루어진다.
- 이때 B 서버의 상태는 **ESTABLISHED**가 된다.

# 4 way handshake

> TCP의 연결을 해제(Connection Termination) 하는 과정

![4-way-handshake](../../images/4-way-handshake.png "4-way-handshake")

### [STEP 1]

- 클라이언트가 연결을 종료하겠다는 FIN 플래그를 전송한다.
- 이때 A 클라이언트는 **FIN-WAIT** 상태가 된다.

### [STEP 2]

- B 서버는 FIN 플래그를 받고 확인 메시지 ACK를 보낸다.
- 그 후 자신의 통신이 끝날때까지 기다리는데 이 상태가 B 서버의 **CLOSE_WAIT** 상태이다.

### [STEP 3]

- 연결을 종료할 준비가 되면, 연결해지를 위한 준비가 되었음을 알리기 위해 클라이언트에게 FIN 플래그를 전송한다.
- 이때 B 서버의 상태는 **LASK-ACK**이다

### [STEP 4]

- 클라이언트는 해지 준비가 되었다는 ACK를 확인했다는 메세지를 보낸다.
- A 클라이언트의 상태가 **FIN-WAIT**에서 **TIME-WAIT** 상태가 된다.

---

## TCP Header 안의 플래그 정보

#### SYN (Synchronize Sequence Number)

- 연결 설정
- Sequence Number를 랜덤으로 설정하여 세션을 연결하는 데 사용하며, 초기에 Sequence Number를 전송한다.
#### ACK (Acknowledgement)

- 응답 확인
- 패킷을 받았다는 것을 의미한다.

#### FIN(Finish)

- 연결 해제
- 세션 연결을 종료시킬 때 사용되며, 더 이상 전송할 데이터가 없음을 의미한다.
