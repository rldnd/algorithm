# FS

## Python

- input(): 한 줄의 문자열을 입력한다.
- map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다.

```py
# 공백을 기준으로 구분된 데이터를 입력 받을 때
data = list(map(int, input().split()))

# 공백을 기준으로 구분된 데이터가 많지 않다면
a, b, c = map(int, input().split())
```

### 파일 입출력

```py
sys.stdin = open("input.txt", "r")
```

### 좀 더 빠르게 입력 받기

- sys.stdin.readline() 사용
- 단, 입력 후 엔터가 사용되므로 rstrip()를 함께 사용

## Javascript

### 입력 값이 한 개일 때 (한 줄)

```js
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
```

### 입력 값이 여러 개일 때 (한 줄에 공백으로 구분)

```js
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
```

### 입력 값이 여러 줄일 때

```js
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
```

### 입력 값이 첫 번째 줄에는 입력 값의 길이(n), 두 번째 줄에 공백으로 구분된 입력값이 주어질 때

```js
const fs = require("fs");
const [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const inputArr = input.trim().split(" ");
```

### 입력 값이 첫 번째 줄에는 입력 값의 길이(n), n개의 줄에 걸쳐서 한 줄에 하나의 입력값이 주어질 때

```js
const fs = require("fs");
const [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
```
