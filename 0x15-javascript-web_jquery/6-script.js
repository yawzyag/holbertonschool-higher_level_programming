const divHeader = $('DIV#update_header');
const header = $('header');

divHeader.on('click', () => {
  header.text('New Header!!!');
});
