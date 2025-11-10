#!/usr/bin/node
// Script to add the class red to the header element when clicking on red_header
document.getElementById('red_header').addEventListener('click', function() {
  document.querySelector('header').classList.add('red');
});
