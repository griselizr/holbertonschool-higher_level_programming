#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (arg) {
    for (let a = 0; a < arg; ++a) {
        console.log('C is fun');
    }

} else {
    console.log('Missing number of occurrences');
}