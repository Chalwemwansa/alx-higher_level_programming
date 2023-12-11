#!/usr/bin/node

function fact (myVar) {
  if (isNaN(myVar) || myVar === 1 || myVar === 0) {
    return (1);
  }
  return myVar * fact(--myVar);
}

const arg = parseInt(process.argv[2], 10);
console.log(`${fact(arg)}`);
