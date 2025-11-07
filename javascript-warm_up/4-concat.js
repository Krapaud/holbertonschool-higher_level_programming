#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 2) {
  console.log(args[0] + ' is ' + args[1]);
}

