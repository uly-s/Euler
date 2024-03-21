let n = 20

const bico = (n) => {
    return factorial(2*n) / Math.pow(Math.factorial(n), 2)
}

for (let i = 0; i < 21; i++) {
    console.log(i + ": " +bico(i));
}



