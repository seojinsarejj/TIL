# AWS 교육 - 2021/01/23

---

# 인스턴스 유형

---

| 인스턴스 유형 패밀리 | 유형 |
| :---: | :---: |
| 범용 | T3,T2,M5,M4 |
| 컴퓨팅 최적화 | C5,C4 |
| 메모리 최적화 | X1e,X1,R5,R4,z1d |
| 가속화된 컴퓨팅 | P3,P2,G3,F1 |
| 스토리지 최적화 | H1,I3,D2 |

- 범용 : 컴퓨팅, 메모리, 네트워크 리소스를 균형있게 제공
- 컴퓨팅 최적화 : 대규모 요청을 받는 웹 서버와 고성능 머신 러닝 워크로드에 사용
- 메모리 최적화 : 처리량이 많은 데이터베이스, 데이터 분석, 캐싱 작업에 유용
- 가속화된 컴퓨팅 : 거성능 범용 그래픽 처리 장치 제공. 3D 시각화/렌더링, 재무 분석, 전산 유체 역학과 같은 높은 부하의 워크로드에 권장
- 스토리지 최적화 : 지연 시간이 짧은 대용량 인스턴스 스토리지 볼륭을 사용. 분산 파일 시스템과 규모가 큰 데이터 처리 애플리케이션에 유용


## 참고

[Amazon EC2 인스턴스 유형 - Amazon Web Services](https://aws.amazon.com/ko/ec2/instance-types/?trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_KR&sc_publisher=Google&sc_category=Cloud%20Computing&sc_country=KR&sc_geo=APAC&sc_outcome=acq&sc_detail=aws%20ec2&sc_content={ad%20group}&sc_matchtype=e&sc_segment=477203497843&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Cloud%20Computing|EC2|KR|EN|Sitelink&s_kwcid=AL!4422!3!477203497843!e!!g!!aws%20ec2&ef_id=Cj0KCQiAjKqABhDLARIsABbJrGlb4VMxRjnwlLlQjyyriUFMXbaURmyJf7Oc9duMRUmDOsJ7v3Fc2UAaAoG0EALw_wcB:G:s&s_kwcid=AL!4422!3!477203497843!e!!g!!aws%20ec2)

# 인스턴스 구성

---

## 인스턴스 결제 방식

- 온디맨드
- Spot Instance
    - AWS에서 유휴자원(놀고있는 컴퓨터)이 많으면 손해겠죠? 때문에 굉장히 싸게 임시 대여해 주는 개념
- RI(Reserved Instance)
    - 피시방 정액제와 비슷한 개념

## 배치 그룹 (placement group)

- 체크 시 최대한 가까운 랙에 배치

    → 서로 통신이 많이 발생할 떄 유용

    → 빠르게 통신 가능 

## 테넌시 (Tenancy)

- Shared - 아무 서버나 남들과 공유해서 써도 됌
- Dedicated -  서버 한대를 다 씀 ( 미리 구입해야함 )

## User data

- 서버 시작 후 실행되는 스크립트

# 스토리지

---

- ec2 = cpu + ram
- ebs = 저장 공간
- 서버 = ec2 + ebs

## IOPS ( Input/Output per Sec)

- 하드웨어를 공유하기 떄문에 한쪽에서 많이 쓰면 다른 쪽에서 많이 쓸 수 없음
- 따라서 읽기 쓰기 속도를 제한함
- IOPS를 초과하면 초과한 만큼 다음 시간으로 넘어감

## Delete on Termination

- ec2를 삭제할 떄 ebs도 함께 삭제할것인가

# 태그

---

- 리소스에 이름을 부여
- key-value로 구성 ( 예 : Name-webserver )

# 보안그룹

---

- 접속 허가 그룹 설정
- 기본적으로 모든것에 대해 제한이 있고 보안그룹 설정에서 허가되는 규칙을 설정함

# Key Pair

---

- 서버에 접속하기 위한 키를 생성
- 다수가 사용한다면 여러 키를 생성하는게 맞는 방법. 하나의 키를 공유 X
- Key Pair Name은 목적 또는 서버 이름과 상관없는 이름을 작성

     → 유출 되었을 시 어떤 서버의 키 페어인지 쉽게 유추가 가능하기 때문

# Cloud9으로 ec2 접속

---

1. cloud9 생성
2. 키페어 등록
3. chmod 400 (키페어이름)
4. 보안그룹 설정
5. ssh -i (키페어이름) ec2-user@(주소)