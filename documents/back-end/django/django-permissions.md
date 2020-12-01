# django permissions

django rest framework는 **권한 검사** 기능을 제공한다.

django rest framework의 permissions.py 그 중 BasePermission은 다음과 같이 이루어져 있다.

```python
class BasePermission(metaclass=BasePermissionMetaclass):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True
        ```
```
BasePermission을 상속받은 대표적인 기본 제공 클래스들은 다음과 같다.

## IsAuthenticated

- 인증된 사용자인지 검사한다.

```python
class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
```

## IsAdminUser

- 어드민 유저인지 검사한다.

```python
class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

```

## IsAuthenticatedOrReadOnly

- 인증된 사용자인가 그렇지 않다면 읽기만 가능하다.

```python
class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
```

- 여기서 **SAFE_METHODS**는 
`SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')`로 이루어져 있다.
- 즉 위 코드는 GET, HEAD, OPTIONS 메소드를 통한 접근은 인증 없이 가능하다는 것`


이렇게 정의된 permissions는 다음 방법으로 사용할 수 있다.

## 글로벌 설정

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

## 뷰마다 설정

```python
permission_classes = [IsAuthenticated]
```

## 데코레이터로 함수 마다 설정
```python
@permission_classes([IsAuthenticated])
```