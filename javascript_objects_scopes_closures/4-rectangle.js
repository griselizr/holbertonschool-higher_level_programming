#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        w = parseInt(w);
        h = parseInt(h);
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        let second = this.height;
        while (second) {
            console.log('X'.repeat(this.width));
            second--;
        }
    }

    double() {
        this.width *= 2;
        this.height *= 2;
    }

    rotate() {
        const third = this.height;
        this.height = this.width;
        this.width = third;
    }
}
module.exports = Rectangle;