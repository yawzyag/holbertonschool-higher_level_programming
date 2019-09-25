#!/usr/bin/node
const request = require('request');

const textA = `http://swapi.co/api/films/${process.argv[2]}`;

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      try {
        resolve(body);
      } catch {
        reject(error);
      }
    });
  });
}

// Usage:

async function main (url) {
  const res = await doRequest(url);
  const json = JSON.parse(res);
  for (const char of json.characters) {
    const res1 = await doRequest(char);
    const json1 = JSON.parse(res1);
    console.log(json1.name);
  }
}

main(textA);
