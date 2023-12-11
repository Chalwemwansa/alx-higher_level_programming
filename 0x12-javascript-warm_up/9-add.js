#!/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return parseInt(a, 10) + parseInt(b, 10);
  }
}
console.log(`${add(process.argv[2], process.argv[3])}`);
