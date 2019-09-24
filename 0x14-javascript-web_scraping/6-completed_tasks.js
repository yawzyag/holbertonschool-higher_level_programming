#!/usr/bin/node
const request = require('request');

const textA = process.argv[2];

request(textA, function (error, response, body) {
  if (error) console.error(error);
  const json = JSON.parse(body);
  const obj = {};
  for (const todo of json) {
    obj[todo.userId] = '';
  }
  let count = 0;
  for (const key in obj) {
    for (const todo of json) {
      if (key === todo.userId.toString() && todo.completed === true) {
        if (obj[key] > 0) count = obj[key];
        else count = 0;
        count++;
        obj[key] = count;
      }
    }
  }
  console.log(obj);
});
