// check if a number is prime
const prime = (x) => {
    for (let i = 2; i <= Math.sqrt(x); i++) {
        if (x % i === 0) return false;
    }
    return true;
} 

// counter variable
let count = 0;

// loop through numbers until we find the 10001st prime
let i = 2;

while(count < 10002) {
    if(prime(i)) {
        count++;
        console.log(count, i);
    }
    i++;
}

//console.log(i - 1);