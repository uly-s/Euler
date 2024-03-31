const fn = 0;

// add for spread
function print(...val) {
    let output = val.length == 1 ? 
        val[0] :
        val.toString().replace(",", " ");
    console.log(output);
}

let obj = {a:1, b:2};
print(1);

// function sum(vals) {
//     // add if vals[0] is a number
//     let total = 0;

//     for (let val of vals) {
//        total += val;
//     }

//     return total;
// }

function prototypes() {

    Array.prototype.sum = function(start=0, end=this.length) {
        if (typeof this[0] !== 'number' || end >= this.length) return;
        let total  = 0;
        for (let i = start; i <= end; i++) total += this[i];
        return total;
    };

}

function range(start, end, step=1) {
    let vals = [];

    for(let i = start; i <= end; i += step)  {
        vals.push(i);
    }

    return vals;
}

// function* range(start, end, step = 1) {
//     let current = start;
//     while (current < end) {
//         yield current;
//         current += step;
//     }
// }

// see if that dumb lambda can be cleaned up
function repeat(n, action, args=undefined) {
    for (let i = 0; i < n; i++) {
      action(args);
    }
}

//repeat(5, print, "YO")
// reusable lambda?

function unless(test, then) {
    if (!test) return then();
}

// unless(1 == 0, () => {
//     print("yo");
// })

function loop(spec, action) {
    for(let i = spec[0]; i < spec[1]; i += spec[2]) {
        action();
    }
}

//loop([0, 10, 1], fn => print("hello world"))

const when = (condition, fn) => {
    if (condition) fn();
  };
  


export {print, range, repeat, unless, loop, when, prototypes};