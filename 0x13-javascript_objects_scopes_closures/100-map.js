#!/usr/bin/node
const { list } = require('./100-data');
const newArray = list.map((num) => num * list.indexOf(num));

print(list);
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
