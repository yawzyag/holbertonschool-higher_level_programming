#!/usr/bin/node
const dict = require('./101-data').dict;

function swap (dict) {
  const ret = {};
  const lista = [];
  for (const key in dict) {
    lista.push(key.toString());
    ret[dict[key]] = [];
  }
  for (const i of lista) {
    for (const key in ret) {
      if ((key === dict[i].toString())) {
        ret[key].push(i);
      }
    }
  }
  return ret;
}

console.log(swap(dict));
