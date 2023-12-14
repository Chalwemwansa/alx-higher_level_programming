#!/usr/bin/node
const array = require('./100-data').list;
const newArray = array.map((num) => num * array.indexOf(num));

print(array);
print(newArray);

function print (list) {
  let myStr = '[';
  for (let i = 0; i < list.length; i++) {
    myStr += ` ${list[i]}`;
    if (!(i === list.length - 1)) {
      myStr += ',';
    }
  }
  myStr += ' ]';
  console.log(myStr);
}
