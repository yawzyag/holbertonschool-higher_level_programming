#!/usr/bin/node
/*
    js console log #
*/
const num = parseInt(process.argv[2]);
let f = [];
function factorial(n) {
  if (n === 0 || n === 1 || isNaN(n)) return 1;
  if (f[n] > 0) return f[n];
  return (f[n] = factorial(n - 1) * n);
}
console.log(factorial(num));
