#!/usr/bin/node
/*
    js console log #
*/
let x
const num = parseInt(process.argv[2])
if (isNaN(num)) {
  console.log('Missing size')
} else {
  for (x = 0; x < num; x++) {
    console.log('X'.repeat(num))
  }
}
