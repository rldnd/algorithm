const fs = require("fs");

const [caseLength, ...cases] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const caseSum = Array(11);
caseSum[0] = 0;
caseSum[1] = 1;
caseSum[2] = 2;
caseSum[3] = 4;

for (let i = 4; i < 11 + 1; i++) {
  caseSum[i] = caseSum[i - 1] + caseSum[i - 2] + caseSum[i - 3];
}

for (const number of cases) {
  console.log(caseSum[number]);
}
