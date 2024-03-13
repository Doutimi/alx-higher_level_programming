#!/usr/bin/node
class Square extends require('./5-square') {
    constructor (size) {
      super(size, size);
    }

    charPrint(c) {
      if (!c) this.print();
      else {
        for (let h = 0; h < this.height; h++) {
          let line = "";
          for (let w = 0; w < this.width; w++) {
            line += c;
          }
          console.log(line);
        }
      }
    }
  }
module.exports = Square
