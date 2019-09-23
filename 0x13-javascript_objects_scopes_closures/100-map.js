#!/usr/bin/node
const list = require('./100-data.js').list;

console.log(list);
const newList = list.map(function (e) {
  return e * list.indexOf(e);
});
console.log(newList);
