# Bubble Sort

## 의미

Bubble Sort는 Selection Sort와 유사한 알고리즘으로 `서로 인접한 두 원소의 대소를 비교하고, 조건에 맞지 않다면 자리를 교환하며 정렬`하는 알고리즘 이다.

이름의 유래로는 정렬 과정에서 원소의 이동이 거품이 수면으로 올라오는 듯한 모습을 보이기 때문에 지어졌다고 한다.

## 구현 방식

1회전에 첫 번째 원소와 두 번째 원소를, 두 번째 원소와 세 번째 원소를, 세 번째 원소와 네 번째 원소를, … 이런 식으로 (마지막-1)번째 원소와 마지막 원소를 비교하여 조건에 맞지 않는다면 서로 교환한다.

1회전을 수행하고 나면 가장 큰 원소가 맨 뒤로 이동하므로 2회전에서는 맨 끝에 있는 원소는 정렬에서 제외되고, 2회전을 수행하고 나면 끝에서 두 번째 원소까지는 정렬에서 제외된다. 이렇게 정렬을 1회전 수행할 때마다 정렬에서 제외되는 데이터가 하나씩 늘어난다.

![bubbleSort](../assets/bubble-sort.gif)

```python
  def bubble_sort(x):
      length = len(x)-1
      for i in range(length):
        for j in range(length-i):
          if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
    return x
```

### Reference

[https://gyoogle.dev/blog/algorithm/Bubble%20Sort.html](https://gyoogle.dev/blog/algorithm/Bubble%20Sort.html)
