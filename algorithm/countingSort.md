# Counting Sort

## 의미

Counting Sort(계수 정렬)은 sorting을 위해 값 끼리 비교를 하는 것이 아닌, `배열의 사이즈를 n으로 만들어 등장하는 수에 해당하는 index에 1씩을 더해주는 방식`이다.

## 장점

버블 정렬, 선택 정렬, 삽입 정렬 같은 경우 시간 복잡도는 O(n^2)이기 때문에 시간 초과가 가능하다.
퀵 정렬, 병합 정렬, 힙 정렬 같은 O(nlogn)의 시간 복잡도를 가지는 알고리즘으로 풀기에도 데이터의 양이 너무 많기에 시간 초과가 발생할 확률이 있다.

시간 복잡도: O(n)
공간 복잡도: O(k)

## 구현 방식

```py
# 입력 예시: 1 3 17 5 7
# 출력 예시: 1 3 5 7 17

# 입력될 수 있는 숫자의 최대 크기
MAX_NUM = 1000

# A는 입력된 숫자를 저장하는 배열
A = list(map(int, input().split()))

# N은 입력된 숫자의 개수
N = len(A)

# 0으로 초기화된 입력될 MAX_NUM+1 길이의 배열 count를 생성
count = [0] * (MAX_NUM + 1)
# count_sum은 누적 합을 저장하는 배열
# 누적 합은 특정 숫자가 결과 수열 B에 들어갈 index를 표현한다고 생각하면 된다.
count_sum = [0] * (MAX_NUM + 1)

# 숫자 등장 횟수 세기
for i in range(0, N):
  count[A[i]] += 1

# 숫자 등장 횟수 누적합 구하기
count_sum[0] = count[0]
for i in range(1, MAX_NUM + 1):
  count_sum[i] = count_sum[i - 1] + count[i]

# B는 정렬된 결과를 저장하는 배열
B = [0] * (N + 1)

for i in range(N-1, -1, -1):
  B[count_sum[A[i]]] = A[i]
  count_sum[A[i]] -= 1

# 수열 A를 정렬한 결과인 수열 B를 출력한다.
result = ""
for i in range(1, N+1):
  result += str(B[i]) + ""

print(result)
```

### Reference

[https://bowbowbow.tistory.com/8](https://bowbowbow.tistory.com/8)

[https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html](https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html)
