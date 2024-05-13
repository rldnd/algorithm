const [lines, ...mazeInfo] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [row, col] = lines.split(" ").map(Number);
const visited = [];
const maze = [];
const steps = [];
const DX = [0, 1, 0, -1];
const DY = [1, 0, -1, 0];

for (let i = 0; i < row; i++) {
  const mazeLine = mazeInfo[i].split("");
  visited.push([]);
  maze.push([]);
  steps.push([]);

  for (let j = 0; j < col; j++) {
    visited[i].push(0);
    maze[i].push(Number(mazeLine[j]));
    steps[i].push(0);
  }
}

const queue = [{ 0: 0 }];
visited[0][0] = 1;
steps[0][0] = 1;

while (queue.length > 0) {
  const [[__row, _col]] = Object.entries(queue.shift());
  const _row = Number(__row);
  for (let i = 0; i < 4; i++) {
    const ny = _row + DY[i];
    const nx = _col + DX[i];
    if (ny < 0 || ny >= row || nx < 0 || nx >= col) continue;
    if (visited[ny][nx] || !maze[ny][nx] || steps[ny][nx]) continue;
    visited[ny][nx] = 1;
    steps[ny][nx] = steps[_row][_col] + 1;
    queue.push({ [ny]: nx });
  }
}

console.log(steps[row - 1][col - 1]);
