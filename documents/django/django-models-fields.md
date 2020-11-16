# Django Model
---

- Django 내장 ORM
- ORM : SQL을 직접 작성하지 않아도 장고 모델을 통해 데이터베이스로 접근한다.


## Field types

### IntegerField
---
-2147483648 ~ 2147483647 까지의 int 값을 저장한다.

### BooleanField
---
true/false 필드

### CharField
---
string 필드 중간정도의 길이까지 지원한다. 더 긴 문자열을 저장하기 위해서는 **TextField** 를 사용한다.

- **max_length** : 최대 길이를 설정합니다.

### DateField
---
날짜를 저장한다. 옵션은 다음과 같다.

- **auto_now** : 개체를 저장할 때마다 필드를 지금으로 자동 설정한다. 
- **auto_now_add** : 개체가 처음 생성될 때 필드를 지금으로 자동 설정한다.

### DateTimeField
---
날짜와 시간을 저장한다.


## Relationship fields


### ForeignKey

N:1 관계에서 사용
```python
models.ForeignKey('self',on_delete=models.CASCADE)
```

#### **on_delete**
- CASCADE : 연쇄 삭제
- PROTECT : ProtectedError로 삭제 방지
- RESTRICT : RestrictedError로 삭제 방지
- SET_NULL : NULL이 허용일 경우 NULL로 처리
- SET_DEFAULT : default값으로 초기화