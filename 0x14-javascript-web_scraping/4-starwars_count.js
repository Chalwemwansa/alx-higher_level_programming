#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let sum = 0;
    const films = JSON.parse(body);
    for (const film of films.results) {
      for (const characters of film.characters) {
        if (characters === character) {
          sum += 1;
	}
      }
    }
    console.log(sum);
  }
});
