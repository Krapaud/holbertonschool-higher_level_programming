#!/usr/bin/node

const arg = process.argv.slice(2);

const n = parseInt(arg[0]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let line = '';
    for (let j = 0; j < n; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
