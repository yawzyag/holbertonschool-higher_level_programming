#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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
