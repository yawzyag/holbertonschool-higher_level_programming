#!/usr/bin/node
const list = require('./100-data.js').list;

console.log(list);
const newList = list.map(e => e * list.indexOf(e));
console.log(newList);
