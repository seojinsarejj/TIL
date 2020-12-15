# Quick Sort

## Quick Sort (퀵 정렬)

![quick-sort-gif](../../images/quick-sort-gif.gif "quick-sort-gif")

### Quick Sort (퀵 정렬) 이란?

- **분할 정복 알고리즘**의 하나
- 합병 정렬(merge sort)과 달리 퀵 정렬은 리스트를 비균등하게 분할한다.
- 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법

#### 과정

- 리스트 안에 있는 한 요소를 선택한다. 이렇게 고른 원소를 피벗(pivot) 이라고 한다.
- 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨진다.
- 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.

  - 분할된 부분 리스트에 대하여 순환 호출을 이용하여 정렬을 반복한다.
  - 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복한다.

- 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.
  - 리스트의 크기가 0이나 1이 될 때까지 반복한다.

![quick-sort-concepts](../../images/quick-sort-concepts.png "quick-sort-concepts")

### Quick sort 알고리즘의 구체적인 개념

퀵 정렬은 다음의 단계들로 이루어진다.

- **분할(Divide)** : 입력 배열을 피벗을 기준으로 비균등하게 2개의 부분 배열(피벗을 중심으로 왼쪽 : 피벗보다 작은 요소들, 오른쪽 : 피벗보다 큰 요소들)로 분할한다.
- **정복(Conquer)** : 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출을 이용하여 다시 분할 정복 방법을 적용한다.
- **결합(Combine)** : 정렬된 부분 배열들을 하나의 배열에 합병한다.
- 순환 호출이 한번 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.

#### 퀵 정렬의 과정

![quick-sort2](../../images/quick-sort2.png "quick-sort2")

- 리스트의 첫 번째 데이터를 피벗 값으로 정한다. (임의의 값)
- 2개의 인덱스 변수(low, high)를 이용해서 리스트를 두 개의 부분 리스트로 나눈다.
- 1회전: 피벗이 5인 경우
  - low는 왼쪽에서 오른쪽으로 탐색, 탐색 중 피벗보다 큰 값을 찾으면 stop
  - high는 오른쪽에서 왼쪽으로 탐색, 탐색 중 피벗보다 작은 값을 찾으면 stop
  - low와 high 값을 교환
  - 이 과정을 low와 high가 엇갈릴 때까지 반복
- 2회전 , 3회전을 위의 방법으로 반복한다.

#### 퀵 정렬의 장단점

- 장점
  - 속도가 빠르다
    - 시간 복잡도로 O(nlog₂n)를 가지는 다른 정렬 알고리즘과 비교했을 때도 가장 빠르다.
  - 추가 메모리 공간을 필요로 하지 않는다.
- 단점
  - 정렬된 리스트에 대해서는 퀵 정렬의 불균형 분할에 의해 오히려 수행시간이 더 많이 걸린다.
  - 피벗 값에 따라 시간복잡도가 크게 달라진다. 이상적인 값을 선택했다면 아주 빠른 시간복잡도를 가지지만 최악으로 선택할 경우 **O(N^2)** 이라는 시간 복잡도를 갖게된다.

### 코드 구현 (파이썬)

```python
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

```

### 퀵 정렬 시간 복잡도

- 최선의 경우
  ![sort-time-complexity-etc1](../../images/sort-time-complexity-etc1.png "sort-time-complexity-etc1")

- **_순환 호출의 깊이 X 각 순환 호출 단계의 비교 연산 = log₂n X n = nlog₂n_**

---

- 최악의 경우

  ![sort-time-complexity-etc2](../../images/sort-time-complexity-etc2.png "sort-time-complexity-etc2")

- **_순환 호출의 깊이 \* 각 순환 호출 단계의 비교 연산 = n^2_**
