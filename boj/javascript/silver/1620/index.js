const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [dictionaryCount, questionCount] = inputs[0].split(" ").map(Number);
const indexAndNameDict = {};
const nameAndIndexDict = {};

for (let i = 0; i < dictionaryCount; i++) {
  item = inputs[i + 1];
  Object.assign(indexAndNameDict, { [i + 1]: item });
  Object.assign(nameAndIndexDict, { [item]: i + 1 });
}

for (let i = 0; i < questionCount; i++) {
  const startPoint = i + dictionaryCount + 1;
  if (Number.isNaN(Number(inputs[startPoint]))) {
    console.log(nameAndIndexDict[inputs[startPoint]]);
  } else {
    console.log(indexAndNameDict[inputs[startPoint]]);
  }
}
