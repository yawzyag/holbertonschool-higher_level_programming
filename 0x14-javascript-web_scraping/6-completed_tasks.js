#!/usr/bin/node
const request = require('request');

const textA = process.argv[2];

request(textA, function (error, response, body) {
  if (error) console.error(error);
  const json = JSON.parse(body);
  const obj = {};
  for (const todo of json) {
    if (todo.completed === true) {
      if (!obj[todo.userId]) obj[todo.userId] = 1;
      else obj[todo.userId]++;
    }
  }
  console.log(obj);
});
