#!/usr/bin/node

if (process.argv.length < 4) {
    console.log('0');
} else {
    const all = process.argv.slice(2);
    all.sort((x, y) => y - x);
    console.log(all[1]);
}
