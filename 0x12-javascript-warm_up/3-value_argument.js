#!/usr/bin/node
/*
    js console log #
*/
var argv = process.argv[2];
if (argv) {
  console.log(argv);
} else {
  console.log("No argument");
}
