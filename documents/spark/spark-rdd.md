# 복원 분산 데이터 집합 (RDD)

복원 분산 데이터 집합 (RDD) 은 스파크 프로그래밍에서 사용되는 가장 기본적인 데이터 객체이다.

RDD는 다음 두 가지 작업을 지원한다.

- 변환(transformation) : 외부 데이터로 RDD를 로드해 연산을 수행한 뒤 새로운 RDD를 생성
- 액션(action) : RDD를 기반으로 궁극적으로 원하는 결과물을 출력해 내는 것. 


## 특징

RDD는 다음과 같은 특성을 지닌다.

### 복원

RDD는 탄력적이다. 스파크에서 작업을 수행하다가 노드가 손실될 경우, 데이터 집합을 재구성할 수 있다.

### 분산

RDD는 분산된다. 각각의 RDD는 여러개의 파티션으로 분리되어 여러 분산 노드에 걸쳐서 저장된다.

### 데이터 집합

RDD는 레코드로 구성된 데이터 집합이다. RDD는 각 파티션이 고유한 레코드 세트를 포함하도록 작성되며,
독립적으로 동작할 수 있다.

### 불변성

RDD는 일단 인스턴스화되고 데이터로 채워진 후에는 업데이트할 수 없다. 
대신 변환 연산을 통해 기존 RDD를 기반으로 새로운 RDD를 생성할 수 있다.


## 예시

RDD에 데이터를 로드하고, 필터 변환을 사용해 새로운 RDD를 생성한 다음, 액션을 사용해 결과 RDD를 디스크에 저장하는 예시이다.

```bash
# 로컬 파일 시스템에서 로그 파일 로드
logfilesrdd = sc.textFile("file:///var/log/hadoop/hdfs/hadoop-hdfs-*")
# 오류에 대해서만 로그 레코드를 필터링하는 변환작업
onlyerrorsrdd = logfilesrdd.filter(lambda line : "ERROR" in line)
#onlyerrorsrdd를 파일로 저장하는 액션작업
onlyerrorsrdd.saveAsTextFile("file:///tmp/onlyerrorsrdd")
```