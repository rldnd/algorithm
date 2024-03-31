const input = Number(
  require("fs").readFileSync("/dev/stdin").toString().trim()
);
const array = Array(input + 1).fill(0);

for (let i = 2; i < input + 1; i++) {
  array[i] = array[i - 1] + 1;
  if (i % 2 === 0) {
    array[i] = Math.min(array[i], array[i / 2] + 1);
  }
  if (i % 3 === 0) {
    array[i] = Math.min(array[i], array[i / 3] + 1);
  }
}

console.log(array[input]);
