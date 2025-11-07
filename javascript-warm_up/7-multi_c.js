#!/usr/bin/node
const arg = process.argv.slice(2);

const n = parseInt(arg[0]);

if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
