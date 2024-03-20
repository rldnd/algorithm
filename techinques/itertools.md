# itertools

## combination

> 조합

```py
from itertools import combinations

numbers = [1,2,3,4,5]

# 출력값
"""
[[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5
"""
print(list(map(list, combinations(numbers, 3))))
```

## permutation

> 순열

```py
from itertools import permutations

numbers = ['1','2','3']

# 출력값
"""
['123', '132', '213', '231', '312', '321']
"""
print(list(map(''.join, permutations(numbers))))
```
