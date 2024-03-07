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

## 문자열

| 메서드                                | 설명                                                                       |
| ------------------------------------- | -------------------------------------------------------------------------- |
| s.endswith(prefix, [,start [,end]])   | 문자열이 prefix로 끝나는 지 검사                                           |
| s.find(sub, [, start [, end]])        | 부분 문자열 sub가 처음으로 나타나는 위치를 찾으며 찾지 못하면 -1을 반환    |
| s.lower()                             | 소문자로 변경                                                              |
| s.replace(old, new, [,maxreplace])    | 부분 문자열 대체                                                           |
| s.split([sep [, maxsplit]])           | sep를 분리 기호로 사용하여 문자열을 분할, maxsplit는 최대 분할 횟수를 지정 |
| s.startswith(prefix, [,start [,end]]) | 문자열이 prefix로 시작하는 지 검사                                         |
| s.strip([chrs])                       | 앞이나 뒤에 나오는 공백문자나 chrs로 지정된 문자를 제거                    |
| s.upper()                             | 대문자로 변경                                                              |
