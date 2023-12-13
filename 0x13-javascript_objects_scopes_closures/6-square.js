#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let myStr = '';
        for (let j = 0; j < this.width; j++) {
          myStr += `${c}`;
        }
        console.log(myStr);
      }
    }
  }
}

module.exports = Square;
