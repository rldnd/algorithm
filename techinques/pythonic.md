# Pythonic

> `파이써닉` 이라는 말은 말그래도 `파이썬스러운` 이라고 생각하면 된다.

## formatting

`f-string`을 사용하여 `print()` 함수 변경

```py
name = "lee"
print(f'My name is {name}') # My name is lee
```

`format`메서드, `%`연산자

```py
a = 2
b = 4
print('{0:>3d} {1:2d}'.format(a, b))
print('%3d %2d' % (a, b))
```

## 수학 함수

> 파이썬에서는 `/`는 정수형 내림이 아니다. 즉 `3 / 5 = 0.6`이 된다.
> 우리가 아는 연산자를 사용하고 싶다면 `//`를 사용해라.

| 함수                  | 설명                                |
| --------------------- | ----------------------------------- |
| abs(x)                | 절댓값                              |
| divmod(x,y)           | (x // y, x % y) 반환                |
| pow(x, y, [, modulo]) | (x \*\* y) % modulo 반환            |
| round(x, [n])         | 10의 -n승의 가장 가까운 수로 반올림 |

## 논리 연산자

python은 다른 언어와 다르게 ||, &&, !을 사용하지 않고 or, and, not을 사용한다.
~~진짜 가지가지 하네..~~

False, None, 0, 빈 문자열은 False 즉, 거짓으로 간주한다.
