# RDD에 데이터 로드하기

스파크 루틴을 시작하기 위해서 최소 하나의 RDD를 초기화해야한다.
초기 RDD는 다음과 같은 여러가지 방법으로 생성될 수 있다.

- 하나 이상의 파일에서 데이터 로드하기
- SQL 또는 NoSQL 데이터 스토어와 같은 데이터 소스에서 데이터 로드하기
- 프로그래밍 방식으로 데이터 로드하기
- 스트림에서 데이터 로드하기


## 하나 이상의 텍스트 파일에서 RDD를 만드는 방법

다음에서 설명하는 방법과 텍스트 파일을 이용해 RDD를 만들 수 있다.

# textFile()

`sc.textFile(name,minPartitions=None, use_unicode=True)`

**textFile()** : 파일, 디렉토리 또는 글로브 패턴에서 RDD를 만드는데 사용된다.

**name** : 파일 시스템 스키마를 포함해 참조될 경로 또는 글로브를 지정한다.

**minPartitions** : 파티션 수를 얼마나 만들지 결정한다.

**use_unicode** : 유니 코드 또는 UTF-8을 문자 인코딩 스키마로 사용할지 여부를 지정한다.


# wholeTextFiles()

`sc.wholeTextFiles(path, minPartitions=None, use_unicode=True)`

wholeTextFiles() 메소드는 여러 파일이 포함된 디렉토리를 읽을 수 있다.


# textFile() VS wholeTextFiles()

wholeTextFiles() : 키와 파일 내용을 표함하는 값으로 구성된 레코드로 표시
textFiles() : 각 파일의 각 라인은 해당 팡리 원본 콘텍스트가 없는 별도의 레코드를 나타낸다.


## 프로그래밍 방식으로 데이터 로드하기

내부 데이터를 이용하는 방법은 다음 메소드를 사용하여 처리합니다.

# parallelize()

`sc.parallelize(c, numSlices=None)`

```python
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
distData = sc.parallelize(data, 5) // 파티션 개수 지정
```

**count()** : 컬렉션의 요소 수를 반환한다.
```python
distData.count() 
9
```

**collect()** : 병렬 컬랙션을 목록으로 반환한다.
```python
[1, 2, 3, 4, 5]
```

# range()

`sc.range(start, end=None, step=1, numSlices=None)`

range() 메소드는 사용자를 위한 목록을 생성하고, RDD를 만들고 배포한다. start,end 및 step 인수는 값의 순서를 정의하고,
numSlices는 원하는 분할 수를 지정한다.

```python
# 0에서 시작하는 1000개의 정수로,2개의 파티션에서 1씩 증가하는 RDD를 만든다
range_rdd = sc.range(0, 1000, 1, 2)

