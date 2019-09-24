#!/usr/bin/node
const request = require('request');

const textA = `http://swapi.co/api/films/${process.argv[2]}`;

request(textA, function (error, response, body) {
  if (error) console.error(error);
  const json = JSON.parse(body);
  for (const char of json.characters) {
    request(char, function (error, response, body) {
      if (error) console.error(error);
      const json1 = JSON.parse(body);
      console.log(json1.name);
    });
  }
});
