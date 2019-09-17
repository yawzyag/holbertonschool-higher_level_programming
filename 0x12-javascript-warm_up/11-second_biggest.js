#!/usr/bin/node
/*
    js console log #
*/
const num = process.argv.slice(2);
if (num.length > 1) {
  console.log(num.sort((a, b) => a - b).slice(-2)[0]);
} else {
  console.log(0);
}
