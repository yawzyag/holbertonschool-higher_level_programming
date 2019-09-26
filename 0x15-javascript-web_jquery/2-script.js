#!/usr/bin/node

const divHeader = $('#red_header');
const header = $('header');

divHeader.on('click', function () {
  header.css('color', '#FF0000');
});
