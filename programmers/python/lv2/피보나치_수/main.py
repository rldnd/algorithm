def solution(n):
    memoized_fibonacci = [0 for _ in range(100001)]
    memoized_fibonacci[1] = 1
    for i in range(2, 100001):
        memoized_fibonacci[i] = (memoized_fibonacci[i - 1] + memoized_fibonacci[i - 2]) % 1234567
        
    return memoized_fibonacci[n]
    