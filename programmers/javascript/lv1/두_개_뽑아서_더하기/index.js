const combinations = (arr, value) => {
  const result = [];
  if (value === 1) return arr.map((v) => [v]);

  arr.forEach((item, index, originArr) => {
    const rest = originArr.slice(index + 1);
    const combination = combinations(rest, value - 1);
    const attached = combination.map((c) => [item, ...c]);
    result.push(...attached);
  });
  return result;
};

function solution(numbers) {
  const summations = combinations(numbers, 2).map((values) => {
    return values[0] + values[1];
  });
  const parsedSummations = Array.from(new Set(summations));
  return parsedSummations.sort((a, b) => a - b);
}
