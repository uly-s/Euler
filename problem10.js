// check if a number {x} is prime
function isPrime(x) {
    for (let i = 2; i <= Math.sqrt(x); i++) {
        if (x % i === 0) {
            return false;
        }
    }
    return true;
};

// generate an array of primes up to {n}
function generatePrimes(n) {
    let primes = [];
    for (let i = 2; i < n; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
};

// get array of primes up to 2 million
let primes = generatePrimes(2000000);

// sum the primes
let sum = primes.reduce((sum, val) => {
    return sum + val;
});

console.log(sum);