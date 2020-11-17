# 레이어드 아키텍처 패턴

- 코드를 논리적인 부분 혹은 역할에 따라 독립된 모듈로 나누어서 구성하는 패턴

## 구성 요소

### **Presentation layer : View**
시스템 사용자, 클라이언트 시스템과 직접 연결되는 부분
다음과 같은 로직을 구현한다.
 - API endpoint 정의
 - 전송된 HTTP request 읽기

### **Control layer : Controller**
구성 요소간의 처리 흐름을 제어, 데이터 조작 의뢰, 데이터 변환 및 연산, Exception과 Error처리

 ### **Business layer : Service**
 비즈니스 로직을 구현하는 부분이다. 

 ### **Persistence layer : DAO**
 데이터베이스와 관련된 로직을 구현하는 부분이다.

## 레이어드 아키텍처 적용

api
|- view : presentation layer - endpoint 정의, request 받기
|- service : business layer - 로직 구현
|- model : persistence layer - 데이터베이스 접속
|- app.py : 앱을 실행해 모든 레이어의 변수들을 연결

