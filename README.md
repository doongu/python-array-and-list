# python-array-and-list
array의 경우
```
from array import array
```
를 통해 쉽게 사용해볼 수 있습니다.

---

### 결과

list와 array의 사이즈를 비교하니 아래와 같은 결과가 나왔습니다.

```
list_rage sizeof :  8000040
arr_large sizeof :  4000064
```

### 결론
python의 __array는 정적 array입니다.__


python의 __list는 동적 array를 구현한 것입니다.__ 그렇기에 array보다 더 많은 공간을 차지합니다.(미리 공간을 할당받기 때문)

그래서 고정된 데이터 크기를 가지고 있다면 array를 사용하는 것이 list에 비해 메모리 유수를 줄일 수 있습니다.