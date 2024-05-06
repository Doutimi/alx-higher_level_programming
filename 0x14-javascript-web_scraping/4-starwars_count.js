#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) console.log(err);
  let list = [];
  for (const film of JSON.parse(body).results) {
    list = list.concat(film.characters);
  }
  const uniq = list.filter(x => x.includes('18'));
  console.log(uniq.length);
});
