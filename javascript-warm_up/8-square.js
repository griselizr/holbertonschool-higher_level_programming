#!/usr/bin/node

const all = parseInt(process.argv[2]);

if (!isNaN(all)) {

    let idx;
    for (idx = 0; idx < all; idx++) {
        console.log('X'.repeat(all));
    }
} else {
    console.log('Missing size');
}
