#!/usr/bin/node

const divHeader = $('DIV#red_header');
const header = $('header');

divHeader.on('click', () => {
  header.addClass('red');
});
