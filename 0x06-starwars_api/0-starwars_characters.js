#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const film= 'https://swapi-api.hbtn.io/api/films/' + movieId;
let  movie_characters = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(film, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      movie_characters = jsonBody.characters;
      resolve();
    }
  }));
};
console.log(movie_characters);