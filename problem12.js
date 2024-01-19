/*
Problem 12
Triangle Numbers
Need 2 functions
1. Find the factors of a number
2. Find the nth triangle number
*/

// find the number of factors of a number (return as an integer)
function factors(x) {
    let count = 0;
    let sqrt = Math.sqrt(x);

    for (let i = 1; i <= sqrt; i++) {
        if (x % i === 0) {
            count += 2; // Count both the divisor and its corresponding quotient
        }
    }

    // If x is a perfect square, subtract one from the count
    if (sqrt * sqrt === x) {
        count--;
    }

    return count;
}

// find the nth triangle number (and return it)
function triangle(n) {
    return (n * (n + 1)) / 2;
}
// get a series of triangle numbers, and list their number of factors
for (let i = 1; i <= 10; i++) {
    //console.log(factors(triangle(i)))
}

let facmax = 0;
let n = 10000;

while (facmax < 500) {
    n++
    facmax = factors(triangle(n));
    console.log();
    console.log(n);
    console.log(facmax);
    console.log(triangle(n));

}



