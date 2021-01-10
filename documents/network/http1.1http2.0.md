# HTTP 1.1 vs HTTP 2.0

![http_compare](../../images/http_compare.png "http_compare")

## HTTP 1.1

1. 연결당 하나의 요청과 응답을 처리한다.

2. 동시전송 문제와 다수의 리소스를 처리하기에 속도와 성능 이슈를 가지고 있다.

3. HOL(Head Of Line) Blocking (특정 응답 지연)

   - 네트워크에서 같은 큐에 있는 패킷이 첫번째 패킷에 의해 지연될 때 발생하는 성능 저하 현상
   - HTTP/1.1의 사양상의 제한으로 클라이언트의 리퀘스트의 순서와 서버의 응답순서는 동기화해야 됨

4. RTT(Round Trip TIme) 증가 (양방향 지연)

5. 헤더가 크다 (특히 쿠키 때문)

## HTTP 2.0

#### HTTP/2.0은 HTTP/1.1이 느려서 버전을 개선한 것

1. **Multiplexed Streams**
   - 한 커넥션에 여러개의 메세지를 동시에 주고 받을 수 있음
2. **Header Compression**
   - Header 정보를 HPACK 압축 방식을 이용하여 압축 전송
3. **Stream Prioritization**
   - 요청 리소스간 의존관계를 설정
   - HTTP 메시지가 많은 개별 프레임으로 분할될 수 있고 여러 스트림의 프레임을 다중화(Multiplexing)할 수 있게 되면서, 스트림들의 우선순위를 지정
4. **Server Push**
   - HTML문서 상에 필요한 리소스를 클라이언트 요청없이 보내줄 수 있음
   - 클라이언트가 요청 하지 않은 JavaScript, CSS, Font, 이미지 파일 등과 같이 필요하게 될 특정 파일들을 서버에서 단일 HTTP 요청 응답 시 함께 전송
