#!/usr/bin/node
// Script to update the text color of the header element to red when clicking on red_header
document.getElementById('red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});