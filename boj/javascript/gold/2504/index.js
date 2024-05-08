const input = require("fs").readFileSync("/dev/stdin").toString().trim();

const charList = input.split("");
const stack = [];

const checkNumberPlus = () => {
  if (stack.length <= 1) return;
  while (typeof stack.at(-1) === "number" && typeof stack.at(-2) === "number") {
    const number = stack.at(-1) + stack.at(-2);
    stack.pop();
    stack.pop();
    stack.push(number);
  }
};

for (let i = 0; i < charList.length; i++) {
  const char = charList[i];
  if (char === "(" || char === "[") {
    stack.push(char);
    continue;
  }
  if (stack.length === 0) {
    console.log(0);
    return;
  }
  if (stack.length > 1) {
    if (
      typeof stack.at(-1) === "number" &&
      stack.at(-2) == "(" &&
      char === ")"
    ) {
      const num = stack.at(-1);
      stack.pop();
      stack.pop();
      stack.push(num * 2);
      checkNumberPlus();
      continue;
    }
    if (
      typeof stack.at(-1) === "number" &&
      stack.at(-2) == "[" &&
      char === "]"
    ) {
      const num = stack.at(-1);
      stack.pop();
      stack.pop();
      stack.push(num * 3);
      checkNumberPlus();

      continue;
    }
  }
  if (stack.at(-1) === "(" && char === ")") {
    stack.pop();
    stack.push(2);
    checkNumberPlus();

    continue;
  }
  if (stack.at(-1) === "[" && char === "]") {
    stack.pop();
    stack.push(3);
    checkNumberPlus();
    continue;
  }
  console.log(0);
  return;
}

if (stack.length !== 1 || typeof stack[0] !== "number") {
  console.log(0);
} else console.log(stack[0]);
