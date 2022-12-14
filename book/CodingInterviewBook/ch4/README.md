# 4장

# 빅오

빅오는 점근적 실행 시간를 표기할 때 가장 널리 쓰이는 수학적 표기법 중 하나이다.

점근적 실행시간 → 시간 복잡도

빅오 표기법에는 시간 복잡도를 표현하는 대표적인 방법이다. 다음의 식을 보자.


**4n^2 + 3n + 4**


해당 식의 최고 차항은 $4n^2$이다. n이 무한이 커지게 되면 최고차항은 나머지 값을 무시할 수 있을 정도로 커진다. 따라서 시간 복잡도는 최고 차항만을 고려하고 나머지는 무시가 된다.

- 시간 복잡도 = O(n^2)

추이에 따른 빅오 표기법의 종류는 크게 다음과 같다.

- ### O(1)
    - 입력값이 아무리 커도 실행 시간은 일정 → 최고의 알고리즘
    - 해시 테이블의 조회 및 삽입이 이에 해당
- ### O(log n)
    - 여기서 부터 입력 값에 영향을 받는다.
    - 로그의 값은 n이 커도 크게 영향 받지않는다.
    - 이진 검색이 이에 해당
- ### O(n)
    - 선형시간 알고리즘이라 불린다.
    - 정렬되지 않는 리스트에서 최대 최솟값을 찾는 경우
- ### O(nlogn)
    - 병합 정렬을 비롯한 대부분의 효율좋은 정렬 알고리즘이 해당
    - 정렬 알고리즘은 이보다 빠를 수 없다.
- ### O(n^2) 
  - 버블 정렬 같은 비효율적인 정렬 알고리즘이 이에 해당
- ### O(2^n)
  - 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당한다.
- ### O(n!)
  - 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제를 브루트 포스로 풀이할 때 해당

# 자료형

## 파이썬 자료형
- ### 숫자
  - 파이썬은 정수형으로 int만 제공한다.
  - 크기가 커지면 자동으로 Long 타입으로 변경된다.
  - bool은 논리 자료형이지만 내부적으로 1(True), 0(False)를 처리하는 int의 서브 클래스다.
- ### 매핑
  - 키와 자료형으로 구성된 복합 자료형
  - 딕셔너리가 유일하다.
- ### 집합
  - 중복된 값을 갖지 않는 자료형
#### 빈집합을 선언
```python
>>> a = set()
>>> a
set()
>>> type(a)
<class 'set'>
```
#### 값이 포함된 집합
```python
>>> a = {'a', 'b', 'c'}
>>> type(a)
<class 'set'>
>>> a = {'a':'A', 'B':'B', 'c':'C'}
>>> type(a)
<class 'dict'>
```
- ### 시퀀스
  - '수열'과 같은 의미를 가진다.
  - str, list가 이것에 속한다.
  #### 불변과 가변 시퀀스
|불변|가변|
|---|---|
|str, tuple, bytes|list|
**불변의 의미는 내부의 요소를 변경할 수 없다는 의미이다.**
