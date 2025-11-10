#!/usr/bin/node
// Script to fetch and display a Star Wars character name
async function displayName () {
  const element = document.getElementById('character');
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
  const data = await response.json();
  element.textContent = data.name;
}
displayName();
