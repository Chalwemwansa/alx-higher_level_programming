#!/usr/bin/node
const num = gene();

function * gene () {
  for (let i = 0; true; i++) {
    yield i;
  }
}

exports.logMe = function (item) {
  console.log(`${num.next().value}: ${item}`);
};
