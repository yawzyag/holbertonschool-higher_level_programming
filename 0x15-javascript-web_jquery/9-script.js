#!/usr/bin/node
$(() => {
  const divHello = $('#hello');
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get({
    url,
    success: (result) => {
      divHello.text(`${result.hello}`);
    }
  });
});
