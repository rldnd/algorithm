const [lines, ...commands] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

class Deque {
  constructor() {
    this.head = 10_002;
    this.tail = 10_002;
    this.list = Array.from({ length: 20_005 }).fill(undefined);
  }

  pushFront(value) {
    this.list[--this.head] = value;
  }

  pushBack(value) {
    this.list[this.tail++] = value;
  }

  size() {
    return this.tail - this.head;
  }

  empty() {
    return this.size() ? 0 : 1;
  }

  front() {
    return typeof this.list[this.head] === "undefined"
      ? -1
      : this.list[this.head];
  }

  back() {
    return typeof this.list[this.tail - 1] === "undefined"
      ? -1
      : this.list[this.tail - 1];
  }

  popFront() {
    if (this.empty()) return -1;
    return this.list[this.head++];
  }

  popBack() {
    if (this.empty()) return -1;
    return this.list[--this.tail];
  }
}

const lineCount = Number(lines);
const deque = new Deque();

for (let i = 0; i < lineCount; i++) {
  const command = commands[i];

  if (command.includes("push_back")) {
    const num = command.split(" ")[1];
    deque.pushBack(Number(num));
  }
  if (command.includes("push_front")) {
    const num = command.split(" ")[1];
    deque.pushFront(Number(num));
  }
  if (command === "front") {
    console.log(deque.front());
  }
  if (command === "back") {
    console.log(deque.back());
  }
  if (command === "size") {
    console.log(deque.size());
  }
  if (command === "pop_front") {
    console.log(deque.popFront());
  }
  if (command === "pop_back") {
    console.log(deque.popBack());
  }
  if (command === "empty") {
    console.log(deque.empty());
  }
}
