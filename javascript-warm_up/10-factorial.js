#!/usr/bin/node

function _factorial(n) {
    if (isNaN(n)) {
        return 1;
    }
    if (n < 0) {
        return -1;
    }
    if (n === 0) {
        return 1;
    } else {
        return n + _factorial(n - 1);
    }
}

console.log(_factorial(process.argv[2]));

