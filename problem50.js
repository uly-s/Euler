/*

The brute force way to do this is going to be to take our list of all primes below 1e6, 
and try to find all primes that are the sum of a consecutive sequence of a given length. 

- outer loop seqs of 2 to n 
    - inner trying to find seqs of length 2
    then were just running our loop
    we want all the sums of sequences of length n, and to check if they're prime 

*/

import {print, prototypes} from "./eloquent.js";
import {isPrime, generatePrimes} from "./euler.js";

prototypes();

const primes = generatePrimes(1000000);


let answer = {
    length: 0,
    index: 0,
    seq: [],
    sum: 0,
}

for (let seq = 2; seq <= 1000; seq++) {

    for(let i = 0; i <= primes.length - seq; i++) {

        let sum = primes.slice(i, i+seq).reduce((acc, val)=>acc+val, 0);

        if (sum > 1000000) break;

        if (seq > answer.length && isPrime(sum) && primes.includes(sum)) {
            answer.length = seq;
            answer.index = i;
            answer.seq = primes.slice(i, i+seq);
            answer.sum = sum;
        }
    }
}

print(primes.slice(78400, -1));
print(answer)
print(answer.seq.reduce((acc,val)=>acc+val,0));

