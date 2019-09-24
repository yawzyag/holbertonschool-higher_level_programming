#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const textA = process.argv[2];
const fileA = process.argv[3];

request(textA, function (error, res, body) {
  if (error) console.error(error);
  fs.writeFile(fileA, body, 'utf8', function (err) {
    if (err) console.log(err);
  });
});
