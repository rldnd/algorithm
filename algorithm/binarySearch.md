# Binary Search

## 의미

탐색 범위를 두 부분으로 분할하면서 찾는 방식

## 장점

처음부터 끝까지 돌면서 탐색하는 것보다 훨씬 빠른 장점을 지님

시간 복잡도
전체 탐색 : O(N)
이분 탐색 : O(logN)

## 진행 방식

우선 정렬을 해야 함
left와 right로 mid 값 설정
mid와 내가 구하고자 하는 값과 비교
구할 값이 mid보다 높으면 : left = mid+1 구할 값이 mid보다 낮으면 : right = mid - 1
left > right가 될 때까지 계속 반복하기

## 구현 방식

### 반복문

```py
def binary_search(target, data):
    data.sort()
    start = 0 			# 맨 처음 위치
    end = len(data) - 1 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return
```

### 재귀

```py
def binary_search(target, start, end):
    if start > end:		 # 범위를 넘어도 못찾는다면 -1을 반환
        return -1

    mid = (start + end) // 2  # 중간값

    if data[mid] == target:	# 중간값의 데이터가 target과 같다면 mid를 반환
        return mid
    elif data[mid] > target: # target이 작으면 왼쪽 탐색
        end = mid - 1
    else:                    # target이 크면 오른쪽 탐색
        start = mid + 1

    return binary_search(target, start, end) # 줄어든 범위를 더 탐색
```
