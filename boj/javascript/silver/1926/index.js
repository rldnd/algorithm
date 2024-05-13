const [lines, ...drawRows] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [row, col] = lines.split(" ").map(Number);
const draw = [];
const visited = [];

for (let i = 0; i < row; i++) {
  draw.push([]);
  visited.push([]);
  const row = drawRows[i].split(" ");
  for (let j = 0; j < col; j++) {
    draw[i].push(Number(row[j]));
    visited[i].push(0);
  }
}

const DX = [0, 1, 0, -1];
const DY = [1, 0, -1, 0];
const res = [];

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (visited[i][j]) continue;
    visited[i][j] = 1;
    if (draw[i][j]) {
      const queue = [{ [i]: j }];
      res.push(1);
      while (queue.length > 0) {
        const [[_row, _col]] = Object.entries(queue.shift());
        for (let k = 0; k < 4; k++) {
          const dy = Number(_row) + DY[k];
          const dx = _col + DX[k];
          if (dx < 0 || dx >= col || dy < 0 || dy >= row) continue;
          if (visited[dy][dx] || !draw[dy][dx]) continue;
          visited[dy][dx] = 1;
          queue.push({ [dy]: dx });
          const num = res.pop();
          res.push(num + 1);
        }
      }
    }
  }
}

if (res.length === 0) {
  console.log(0);
  console.log(0);
} else {
  console.log(res.length);
  console.log(Math.max(...res));
}
