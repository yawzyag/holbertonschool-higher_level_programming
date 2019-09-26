#!/usr/bin/node

const divchar = $('DIV#character');
$.get({
  url: 'https://swapi.co/api/people/5/?format=json',
  success: (result) => {
    divchar.text(result.name);
  }
});
