#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const film= 'https://swapi-api.hbtn.io/api/films/' + movieId;
let  movie_characters_urls = [];
let character_names = [];

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
const getCharacterNames = async () => {
    if (movie_characters_urls.length > 0) {
      for (const url of movie_characters_urls) {
        await new Promise(resolve => request(url, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            console.error('Error: ', err, '| StatusCode: ', res.statusCode);
          } else {
            const jsonBody = JSON.parse(body);
            character_names.push(jsonBody.name);
            resolve();
          }
        }));
      }
    } else {
      console.error('Error: Could not get character names.');
    }
  };
  
requestCharactersURLs()
getCharacterNames()
console.log(character_names)