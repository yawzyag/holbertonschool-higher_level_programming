#!/usr/bin/node
const request = require('request');

const textA = process.argv[2];

request(textA, function (error, response) {
  if (error) console.error('error:', error);
  else console.log('code:', response && response.statusCode);
});
