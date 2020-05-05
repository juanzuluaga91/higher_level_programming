#!/usr/bin/node
const argLen = process.argv;

if (argLen[2] === undefined) {
    console.log('No argument');
} else {
    console.log(`${argLen[2]}`);
}
