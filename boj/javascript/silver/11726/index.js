const n = Number(require("fs").readFileSync("/dev/stdin").toString().trim());
const values = Array(1001);
values[1] = 1;
values[2] = 2;

for (let i = 3; i < values.length; i++) {
  values[i] = (values[i - 1] + values[i - 2]) % 10_007;
}

console.log(values[n]);
