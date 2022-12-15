#!/usr/bin/node
const file = process.argv.slice(2);
const fs = require('fs');
fs.readFile(String(file), 'utf8', function (err, data) {
    if (err) {
        return console.log(err);
    }
    console.log(data);
});
