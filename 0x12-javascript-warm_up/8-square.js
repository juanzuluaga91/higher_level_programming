#!/usr/bin/node
const times = Number(process.argv[2]);
const x = 'x';
if (!times) {
  console.log('Missing size');
} else {
  for (let index = 0; index < times; index++) {
    console.log(x.repeat(times));
  }
}
