/*

The brute force way to do this is going to be to take our list of all primes below 1e6, 
and try to find all primes that are the sum of a consecutive sequence of a given length. 

- outer loop seqs of 2 to n 
    - inner trying to find seqs of length 2
    then were just running our loop
    we want all the sums of sequences of length n, and to check if they're prime 

*/

const {print} = require("./eloquent.js");
const {isPrime, generatePrimes} = require("./euler.js")

const primes = generatePrimes(100);

print(primes);

for (let seq = 2; seq < 10; seq++) {
    for(let prime = 0 of primes)
}