const divHeader = $('DIV#toggle_header');
const header = $('header');

divHeader.on('click', () => {
  header.toggleClass('red green');
});
