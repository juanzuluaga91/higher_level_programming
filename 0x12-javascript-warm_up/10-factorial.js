#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return factorial(n - 1) * n;
}
let printFactorial;
const x = Number(process.argv[2]);
if (isNaN(x)) {
  printFactorial = 1;
} else {
  printFactorial = factorial(x);
}
console.log(printFactorial);
