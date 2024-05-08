// () => 쌓여있는 스택의 length 만큼 count를 더함
// ) => 1을 더함

const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const charList = input.split("");

const stack = [];
let count = 0;

for (let i = 0; i < charList.length; i++) {
  if (charList[i] === "(" && charList[i + 1] === ")") continue;
  if (i > 0 && charList[i - 1] === "(" && charList[i] === ")") {
    count += stack.length;
    continue;
  }
  if (charList[i] === "(") {
    stack.push("(");
  } else {
    stack.pop();
    count += 1;
  }
}

console.log(count);
