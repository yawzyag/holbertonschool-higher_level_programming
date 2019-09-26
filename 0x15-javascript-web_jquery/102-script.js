#!/usr/bin/node
$(() => {
  const inputBtn = $('INPUT#btn_translate');
  inputBtn.on('click', () => {
    const inputLanguage = $('INPUT#language_code').val();
    const divHello = $('#hello');
    const url = `https://fourtonfish.com/hellosalut/?lang=${inputLanguage}`;

    $.get({
      url,
      success: (result) => {
        divHello.text(`${result.hello}`);
      }
    });
  });
});
