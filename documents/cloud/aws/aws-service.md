# AWS Service

## 컴퓨팅

### Elastic Compute Cloud (EC2)
- `로컬 데이터 센터에서 실행되는 서버를 가상 버전으로 옮겨 놓은 것`
- EC2 인스턴스는 `CPU`, `메모리`, `스토리지`, `네트워크 인터페이스` 프로파일로 프로비저닝해 간단한 웹 서버에서 부터 멀티 티어 아키텍처의 인스턴스 클러스터에 이르기까지 어떤 애플리케이션 요구라도 충족할 수 있다. 

### Lambda
- `서버리스 애플리케이션 아키텍처`
- 사용 시 연중무휴로 운영하지 않더라도 요청을 처리 할 수 있는 퍼블릭 서비스를 제공할 수 있다.
- 이 서비스는 소비자 요청과 같은 네트워크를 통한 이벤트가 있어야 미리 정의된 코드 기반 작업을 작동시킬 수 있다.

### Auto Scaling 
- `기존 인스턴스가 클라이언트의 수요에 대응할 수 없을 때 자동으로 인스턴스를 시작(또는 수직 확장)`할 수 있다.
- 수요가 감소하면 사용하지 않는 인스턴스를 종료(또는 축소)할 수 있다.

### Elastic Load Balancing
- 서버 한 대에만 과부화가 걸리고 다른 서버는 사용률이 낮은 경우 또는 장애가 발생한 서버로 네트워크 트래픽이 전달되는 경우가 발생하지 않도록 유입되는 `네트워크 트래픽을 여러 대의 웹서버로 전송`


### Elastic Beanstalk
- `AWS 컴퓨팅과 네트워킹 인프라를 프로비저닝하는 작업을 추상화`한 관리형 서비스
- 필요한 모든 서비스를 자동으로 시작하고 관리한다.

## 네트워킹 

### Virtual Private Cloud (VPC)
- EC2나 RDS `인스턴스를 호스팅하기 위해 설계`됐다.
- VPC 도구를 사용해 인스턴스의 인바운드 및 아웃바운드 네트워크 엑세스나 인스턴스 간 네트워크 엑세스를 세밀하게 제어할 수 있다.

### Direct Connect
- `타사 공급자가 제공하는 네트워크를 통해 AWS에 빠르고 안전하게 연결`할 수 있다.
- 로컬 데이터 센터 혹은 사무실과 AWS VPC 간에 향상된 직통 터널을 구축할 수 있다.

### Route 53
- `도메인 등록`, `레코드 관리`, `라우팅 프로토콜`, `상태 검사`를 관리할 수 있는 `AWS DNS 서비스`
- 다른 AWS 리소스와 완벽하게 통합돼 있다.

### CloudFront
- Amazon이 제공하는 `분산 글로벌 콘텐츠 전송 네트워크`
- CloudFront 배포를 적절하게 구성해서 사이트 콘텐츠의 캐싱 버전을 전 세계 엣지 로케이션에 저장하고 사용자가 요청할 때 최고 효율성과 짧은 지연 시간으로 콘텐츠를 제공할 수 있다.

## 스토리지

### Simple Storage Service (S3)
- 저렴하고 안정적인 `다목적 객체 스토리지` 제공
- 데이터 스토리지와 백업 용도에 적합

### Glacier
- 저렴하게 장기 저장할 수 있는 `대형 데이터 아카이브`를 제공
- 데이터를 추출할 때 몇 시간이 걸려도 무장할 떄 적합

### Elastic BLock Store (EBS)
- EC2 인스턴스 OS와 작업 데이터를 호스팅하는 `가상의 데이터 드라이브`
- 물리 서버의 스토리지 드라이브와 파티션이라는 개념을 사용

### Storage Gateway
- AWS 클라우드 스토리지를 로컬 온프레미스 어플라이언스처럼 사용하는 `하이브리드 스토리지 시스템`
- 스토리지 게이트웨이는 마이그레이션 및 데이터 백업에 훌륭한 도구이며 재해 복구 작업에 사용할 수 있다.

## 데이터베이스

### Relational Database Service (RDS)
- 안정적이고, 안전하며, 신뢰성 있는 `데이터베이스 인스턴스`를 구축 할 수 있게 하는 관리형 서비스다. 
- MySQL, MS-SQL, Oracle, Amazon이 자체 개발한 Aurora 등 다양한 `SQL 데이터베이스 엔진`을 RDS에서 실행할 수 있다.

### DynamoDB
- 빠르고 유연하고 확장성이 뛰어난 관리형 서비스로 `비관계형(NoSQL) 데이터베이스` 워크로드에 적합하다.

## 애플리케이션 관리

### CloudWatch
- 이벤트룰 통해 `프로세스 성능 및 활용률을 모니터링`하고 사전 설정된 임곗값에 이르면 `메시지 발송이나 자동화된 작업을 트리거`하도록 설정할 수 있다.
  
### CloudFormation
- `복잡한 AWS 배포를 템플릿 파일에 완벽하게 정의`할 수 있다. 

### CloudTail
- `계정 내 모든 API 이벤트 기록을 수집`한다. 
- 이 기록은 계정을 감사하고 문제를 해결하는 데 유용하다.

## 보안과 자격 증명

### Identity and Access Management (IAM)
- `AWS 계정의 사용자`, `프로그래밍 방식 액세스`, `인증`을 관리
- 사용자, 그룹, 역할, 정책을 사용해서 AWS 리소스에 액세스하고 작업할 수 있는 사람과 대상을 정확하게 제어할 수 있다.
  
### Key Management Service (KMS) 
- `AWS 리소스의 데이터를 보호하는 암호화 키를 생성`하고 `키 사용을 관리하는 관리형 서비스`이다.