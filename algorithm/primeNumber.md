# 소수 구하기

## 소수란?

> 소수(`prime number`)는 양의 약수가 ( 1보다 큰 자연수 ) 1과 자기 자신만을 약수로 가지는 수를 의미한다. <-> 합성 수

## 에라토스테네스의 체

`에라토스테네스의 체`는 소수를 찾는 빠르고 쉬운 방법이다.
![에라토스테네스의 체](../assets/sieve-of-eratosthenes.gif)

1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
1. 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
1. 자기 자신을 제외한 2의 배수를 모두 지운다.
1. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
1. 자기 자신을 제외한 3의 배수를 모두 지운다.
1. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
1. 자기 자신을 제외한 5의 배수를 모두 지운다.
1. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
1. 자기 자신을 제외한 7의 배수를 모두 지운다.
1. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다. (보라색)

## 구현 방법

```py
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```

### References

[https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98\_%EC%B2%B4](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
