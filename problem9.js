let squares = [];

for (let i = 0; i < 1000; i++) {
    squares.push(i * i);
};

let triplets = [];

const addTriplet = (a, b, c) => {
    triplets.push([a, b, c]);
};

for (let a = 1; a < 1000; a++) {
    
    for (let b = a; b < 1000; b++) {
        
        let c2 = a*a + b*b; 
        let c = Math.sqrt(c2);
        
        if(squares.includes(c2)) {
            triplets.push([a, b, c]);
        }
    };
};

console.log(triplets);

let the_triplet = triplets.filter((item) => {
    return item[0] + item[1] + item[2] === 1000;
});

console.log(the_triplet);

let the_triplet_product = the_triplet[0][0] * the_triplet[0][1] * the_triplet[0][2];

console.log(the_triplet_product);