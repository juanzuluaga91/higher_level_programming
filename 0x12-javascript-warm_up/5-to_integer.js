#!/usr/bin/node
const argLen = process.argv;

if (Number(argLen[2])) {
  console.log(`My number: ${Number(argLen[2])}`);
} else {
  console.log('Not a number');
}
