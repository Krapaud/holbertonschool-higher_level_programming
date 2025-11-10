#!/usr/bin/node
// Script to add a li element to a list when clicking on add_item
document.getElementById('add_item').addEventListener('click', function() {
    const newitem = document.createElement('li');
    newitem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newitem);
});
