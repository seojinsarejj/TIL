# 해시테이블

> 해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠르게 데이터를 검색할 수 있는 자료구조

- 삽입, 삭제, 검색의 시간복잡도는 O(1)이다.

![hash-table](../../images/hash-table.png "hash-table")

## 구성

### 키 (key)

- 고유한 값으로 해시 함수의 input이 된다.
- 다양한 길이의 값이 될 수 있으므로 공간의 효율성을 위해 해시 함수로 값을 바꾸어야 한다.

### 해시함수 (Hash Function)

- 키 (key)를 해시 (hash)로 바꿔주는 역할이다.
- 서로 다른 키가 같은 해시가 되는 경우를 해시 충돌 (Hash Collision)이라고 한다.

### 해시 (Hash)

- 해시 함수의 결과물이다.
- 저장소 (bucket, slot)에서 값과 매칭되어 저장된다.

### 값 (Value)

- 저장소에 최종적으로 저장되는 값이다
- 키와 매칭되어 저장, 삭제, 검색, 접근이 가능해야 한다.

## Hash Collision (해시 충돌)

> 서로 다른 키가 같은 해시 값이 되어 충돌이 일어나는 경우가 발생한다.

### 해결

#### Chaining

- 자료 저장 시, 저장소에서 충돌이 일어나면 해당 값을 기존 값과 연결시키는 기법이다.

#### Open Addressing (개방주소법)

- 데이터의 해시가 변경되지 않았던 chaining과 달리 비어있는 해시를 찾아 데이터를 저장하는 기법이다.
