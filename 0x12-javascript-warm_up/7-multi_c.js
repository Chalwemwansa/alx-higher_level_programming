#!/usr/bin/node
const myVar = 'C is fun';
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log(myVar);
  }
}
