#!/usr/bin/node
exports.esrever = function (list) {
  let reversedlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedlist = reversedlist.concat(list[i]);
  }
  return reversedlist;
};
