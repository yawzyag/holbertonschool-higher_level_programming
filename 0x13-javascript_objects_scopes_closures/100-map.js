#!/usr/bin/node
const list = require('./100-data.js').list;

const newList = list.map((e, indx) => e * indx);
console.log(list);
console.log(newList);
