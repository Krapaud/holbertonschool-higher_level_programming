#!/usr/bin/node
// Script to fetch and display a translation of "hello"
document.addEventListener('DOMContentLoaded', function () {
  async function displayValue () {
    const element = document.getElementById('hello');
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    const value = await response.json();
    element.textContent = value.hello;
  }
  displayValue();
});
