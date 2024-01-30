#!/usr/bin/node
const request = require('request');

const path = process.argv[2];

request(path, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
