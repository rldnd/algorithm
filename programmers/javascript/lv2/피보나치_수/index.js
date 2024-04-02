function solution(n) {
  const memoizedFibonacci = [0, 1];

  for (let i = 2; i < 100001; i++) {
    memoizedFibonacci[i] =
      (memoizedFibonacci[i - 1] + memoizedFibonacci[i - 2]) % 1234567;
  }

  return memoizedFibonacci[n];
}
