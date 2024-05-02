const [count, ...numbers] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const list = [];

for (item of numbers) {
  if (!item) list.pop();
  else list.push(item);
}

let result = 0;
for (number of list) {
  result += number;
}

console.log(result);
