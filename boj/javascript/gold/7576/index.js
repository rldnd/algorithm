const [MN, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [M, N] = MN.split(" ").map(Number);
const tomatoes = input.map((v) => v.split(" ").map(Number));
const queue = [];
const offsetX = [0, 0, -1, 1];
const offsetY = [-1, 1, 0, 0];

let output = 0;
let pointer = 0;
let zeroCount = 0;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (tomatoes[i][j] === 1) {
      queue.push({ x: j, y: i, count: 0 });
    } else if (tomatoes[i][j] === 0) {
      zeroCount++;
    }
  }
}

while (pointer < queue.length) {
  const { x, y, count } = queue[pointer++];
  for (let i = 0; i < 4; i++) {
    const nx = x + offsetX[i];
    const ny = y + offsetY[i];
    if (tomatoes?.[ny]?.[nx] === 0) {
      queue.push({ x: nx, y: ny, count: count + 1 });
      zeroCount--;
      tomatoes[ny][nx] = 1;
      output = Math.max(output, count + 1);
    }
  }
}

console.log(zeroCount ? -1 : output);
