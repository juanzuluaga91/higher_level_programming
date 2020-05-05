#!/usr/bin/node
const agrs = process.argv;
const argLen = process.argv.length;
let pValue;
if (Number(argLen) <= 3) {
  console.log(1);
} else {
  agrs.shift();
  agrs.shift();
  pValue = agrs.sort(function (a, b) { return b - a; });
  console.log(Number(pValue[1]));
}
