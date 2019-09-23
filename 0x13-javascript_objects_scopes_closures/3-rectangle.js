#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x;
    for (x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
