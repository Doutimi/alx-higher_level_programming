#!/usr/bin/node
// prints all characters of a Star Wars movie synchronously
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);

  const charactersUrls = film.characters;

  const charactersPromises = charactersUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        const character = JSON.parse(body);

        resolve(character.name);
      });
    });
  });

  Promise.all(charactersPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
