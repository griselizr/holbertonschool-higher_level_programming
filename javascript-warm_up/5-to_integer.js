#!/usr/bin/node
const my_num = parseInt(process.argv[2]);

if (my_num) {
    console.log('My number: ' + my_num);
} else {
    console.log('Not a number');
}