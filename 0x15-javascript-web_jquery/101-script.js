#!/usr/bin/node
$(() => {
  const addITem = $('DIV#add_item');
  const rmItem = $('DIV#remove_item');
  const clearList = $('DIV#clear_list');
  const ulList = $('UL.my_list');

  addITem.on('click', () => {
    ulList.append('<li>Item</li>');
  });

  rmItem.on('click', () => {
    $('UL.my_list li:last-child').remove();
  });

  clearList.on('click', () => {
    ulList.empty();
  });
});
