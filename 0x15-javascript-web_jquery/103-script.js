$(() => {
  const req = (languaje) => {
    const divHello = $('#hello');
    const url = `https://fourtonfish.com/hellosalut/?lang=${languaje.val()}`;

    $.get({
      url,
      success: (result) => {
        divHello.text(`${result.hello}`);
      }
    });
  };

  const inputBtn = $('INPUT#btn_translate');
  const inputLanguage = $('INPUT#language_code');
  inputBtn.on('click', () => {
    req(inputLanguage);
  });
  inputLanguage.keyup((e) => {
    if (e.which === 13) {
      req(inputLanguage);
    }
  });
});
