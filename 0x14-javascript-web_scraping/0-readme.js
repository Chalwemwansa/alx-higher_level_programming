#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
