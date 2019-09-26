#!/usr/bin/node

const addITem = $('DIV#add_item');
const ulList = $('UL.my_list');

addITem.on('click', () => {
  ulList.append('<li>Item</li>');
});
