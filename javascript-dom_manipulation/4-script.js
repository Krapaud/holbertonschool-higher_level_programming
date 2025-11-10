#!/usr/bin/node
// Script to add a li element to a list when clicking on add_item
document.getElementById('add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
