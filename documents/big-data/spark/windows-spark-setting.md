# 윈도우에서 스파크 설치하기
>참고: Data Analytics whit SPARK Using PYTHON

## 파이썬 설치




## 자바 설치

최신 오라클 JDK를 다운로드해 설치한다.

```bash
java -version
```
위 명령어를 통해 설치 확인 가능하다.

## 하둡 릴리스 다운로드 및 압축 해제

http://hadoop.apache.org/releases.html 에서 최신 하둡 릴리스를 다운로드한 후
C:\Hadoop과 같은 로컬 디렉토리에 하둡 릴리스 압축을 푼다





## 윈도우용 하둡 바이너리 설치

윈도우에서 스파크를 실행하려면 hadoop.dll 및 winutils.exe를 포함해 윈도우용으로 컴파일된 
여러 하둡 바이너리가 필요하다.

https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-winutils 에서 얻을 수 있다.

다운로드한 hadoop-winutils 아카이브를 C:\Hadoop\bin 에 압축을 푼다




## 스파크 다운로드 및 압축 해제

http://spark.apache.org/downloads.html 에서 최신 스파크 릴리스를 다운로드한 후
C:\Spark와 같은 로컬 디렉토리에 스파크 릴리스 압축을 푼다.




## IPv6 비활성화하기.

```bash
C:\> setx _JAVA_OPTIONS "-Djava.net.preferIPv4Stack=true"
```




## 환경 변수 설정

```bash
C:\> setx HADOOP_HOME C:\Hadoop
```




## 로컬 메타스토어 설정하기

```bash
C:\> mkdir C:\tmp\hive
C:\> hadoop\bin\winutils.exe chmod 777 /tmp/hive
```




## 설치 테스트

pyspark 명령을 입력해 대화형 파이썬 스파크 셸을 연다

```bash
C:\> cd C:\Spark\bin
C:\> pyspark --master local
```

quit()을 입력해 셸을 종료한다
다음을 실행해 내장된 Pi Estimator 샘플 응용 프로그램을 실행한다.

```bash
C:\Spark\bin> spark-submit --class org.apache.spark.examples.SparkPi 
--master local C:\Spark\examples\jars\spark-examples*.jar 100
```

많은 로그 메시지 중 다음과 유사한 내용을 찾는다
```bash
Pi is roughly 3.1413223141322315
```



축하한다! 윈도우에서 스파크를 성공적으로 설치하고 테스트했다.
