#!/usr/bin/node
exports.esrever = function (list) {
    let i = 0;
    const todo = [];
    let num = 0;
    for (i = list.length; i > 0; i--) {
        todo[num] = list[i - 1];
        num++;
    }
    return (todo);
};