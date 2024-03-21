const {print, range} = require("./eloquent.js");
 
const factorial = n => {
    let result = BigInt(n);
    for(let i = BigInt(n-1); 0 < i; i--) {
        print(i);
        result *= i;
    }
    return result;
}

let num = BigInt(factorial(100)).toString();

let sum = [...num].map(val => parseInt(val)).reduce((acc, val) => acc + val, 0);

print(sum);
