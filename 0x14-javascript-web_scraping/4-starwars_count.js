#!/usr/bin/node
const request = require('request');

const textA = `${process.argv[2]}`;

request(textA, function (error, response, body) {
  if (error) console.error(error);
  const json = JSON.parse(body);
  let count = 0;
  let title;
  let char;

  for (title of json.results) {
    for (char of title.characters) {
      if (char.includes('18')) count++;
    }
  }
  console.log(count);
});
