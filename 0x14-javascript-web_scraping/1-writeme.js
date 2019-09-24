#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2]; const textB = process.argv[3];

fs.writeFile(fileA, textB, 'utf8', function (err) {
  if (err) console.log(err);
});
