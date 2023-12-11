#!/usr/bin/node

let secondLargest = 0;
let largest = 0;
const len = process.argv.length;

for (let i = 1; i < len; i++) {
  const num = parseInt(process.argv[i], 10);
  if (largest < num) {
    secondLargest = largest;
    largest = num;
  }
}
console.log(secondLargest);
