#!/usr/bin/node
// Script to update the text of the header element when clicking on update_header
document.getElementById('update_header').addEventListener('click', function () {
  const headerElement = document.querySelector('header');
  headerElement.textContent = 'New Header!!!';
});
