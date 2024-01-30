#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let sum = 0;
    const films = JSON.parse(body);
    for (const film of films.results) {
      for (const characters of film.characters) {
        const charUrl = characters.split('/').filter(n => n !== '');
        const id = charUrl[charUrl.length - 1];
        if (id === '18') {
          sum += 1;
        }
      }
    }
    console.log(sum);
  }
});
