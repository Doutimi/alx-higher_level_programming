#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const nWidth = this.height;
    const nHeight = this.width;
    this.width = nWidth;
    this.height = nHeight;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
