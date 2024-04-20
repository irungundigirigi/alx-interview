#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const film= 'https://swapi-api.hbtn.io/api/films/' + movieId;
let  movie_characters_urls = [];

const requestCharactersURLs = async () => {
  await new Promise(resolve => request(film, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      movie_characters_urls = jsonBody.characters;
      resolve();
    }
  }));
};

requestCharactersURLs()
console.log(movie_characters_urls);