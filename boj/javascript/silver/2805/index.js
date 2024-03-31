const fs = require("fs");
const [inputs, treeInputs] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [treeCount, treeHeight] = inputs.split(" ").map(Number);
const trees = treeInputs
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const getHeight = (value) =>
  trees.reduce((acc, cur) => (acc += Math.max(cur - value, 0)), 0);

let start = 0;
let end = Math.max(...trees);
let middle = 0;

while (start <= end) {
  middle = Math.floor((start + end) / 2);

  if (treeHeight > getHeight(middle)) {
    end = middle - 1;
  } else {
    start = middle + 1;
  }
}

console.log(end);
