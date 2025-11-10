#!/usr/bin/node
// Script to update the text of the header element when clicking on update_header
document.getElementById('update_header').addEventListener('click', function() {
    const headerelement = document.querySelector('header');
    headerelement.textContent = 'New Header!!!';
});
