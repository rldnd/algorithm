const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const LEFT_PARENTHESES = ["(", "["];
const RIGHT_PARENTHESES = [")", "]"];

const getLineResult = (value) => {
  const stack = [];
  for (let i = 0; i < value.length; i++) {
    if (LEFT_PARENTHESES.includes(value[i])) {
      stack.push(value[i]);
    }
    if (RIGHT_PARENTHESES.includes(value[i])) {
      while (true) {
        if (stack.length === 0) return "no";
        if (stack.at(-1) === "(" && value[i] === ")") {
          stack.pop();
          break;
        }
        if (stack.at(-1) === "[" && value[i] === "]") {
          stack.pop();
          break;
        }
        return "no";
      }
    }
  }
  if (stack.length > 0) return "no";
  return "yes";
};

for (const line of input) {
  if (line === ".") return;
  const charList = line.split("");
  console.log(getLineResult(charList));
}
