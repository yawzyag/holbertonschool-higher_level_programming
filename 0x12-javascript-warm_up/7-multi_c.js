#!/usr/bin/node
let x;
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
