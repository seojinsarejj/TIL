# CI/CD (지속적 통합/지속적 제공)

#### **DevOps 엔지니어의 핵심 업무**

## CI (Continuous Integration)

- 지속적 통합
- 새로운 코드 변경 사항이 정기적으로 빌드 및 테스트 되어
  공유 레포지토리에 통합히는 것

### 조건

- 다수의 개발자가 형상관리 툴을 공유하여 사용하는 환경
- MSA(Micro Service Archietecture) 환경
  - MSA : 작은 기능별로 서비스를 잘게 쪼개어 개발하는 형태

### 목표

- 버그를 신속하게 찾아 해결
- 소프트웨어의 품질을 개선
- 새로운 업데이트의 검증 및 릴리즈의 시간을 단축

## CD (Continuous Delivery & Continuous Deployment)

- 지속적인 서비스 제공 혹은 지속적인 배포
- 개발자의 변경 사항이 레포지토리를 넘어, 고객의 프로덕션(Production) 환경까지 릴리즈 되는 것
- 서비스의 사용자는 최대한 빠른 시간 내에 최신 버전의 Production을 제공받을 필요가 있다.
- 개발팀과 비즈니스팀(영업, CS팀 등) 간의 커뮤니케이션 부족 문제를 해결

## 대표적인 CI/CD 툴

- Jenkins
- Travis CI
- Bamboo
- CircleCI
