#!/usr/bin/node

const divUl = $('UL#list_movies');
$.get({
  url: 'https://swapi.co/api/films/?format=json',
  success: (result) => {
    for (const elem of result.results) {
      divUl.append(`<li>${elem.title}</li>`);
    }
  }
});
