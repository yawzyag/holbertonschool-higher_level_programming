#!/usr/bin/node
const Square1 = require('./5-square.js');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) return super.print();
    else {
      let x;
      for (x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
