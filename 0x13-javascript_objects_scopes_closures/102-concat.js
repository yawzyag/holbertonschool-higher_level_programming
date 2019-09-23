#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2]; const fileB = process.argv[3]; const fileC = process.argv[4];

const fileTextA = fs.readFileSync(fileA);
const fileTextB = fs.readFileSync(fileB);

fs.writeFileSync(fileC, fileTextA + fileTextB);
