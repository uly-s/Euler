from math import sqrt, log10, floor, ceil

count = 0
rep = 0

def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

for i in range(1, 1000):
    count += 1
    # testing the recurrence relation with exception
    # I should only see pass, a fail means that on a round of 19 or 24, the rule did not hold
    # except maybe if my counting is off.
    # rule = len(str(fib(i + 5))) == len(str(fib(i))) + 1
    # if count % 19 == 0 or count % 24 == 0 and not rule:
    #     print(i, "pass")
    # elif count % 19 == 0 or count % 24 == 0 and rule:
    #     print(i,"fail")
    #print(i, len(str(fib(i))))

"""
The 7nth term is the first with 2 digits
the 12th with 3
What I want to see is if this can be tackled as a 'series problem'
I.e. "each 5 fibonacci numbers will have the same number of digits after the 39th number"
that's a recurrence rule, => len(str(fib(i + 5))) == len(str(fib(i))) + 1
(Note, if you didn't know the term recurrence rule, you would have struggled to come up with the code for that)
it's not exact but quite close (for numbers of 3 digits) it seems to follow a skip rule => every 19th, 24th, 24th digit will not follow the recurrence rule
If it follows out to 5/6 digits, it should work out until 1000, maybe.
But ideally there's a way to simply define an explicit function...
You're still trying to come up with approximation methods and guessing and checking results rather than being able to properly math out the result.
I can be relatively certain that roughly the 5000nth digit will have 1000 digits, and guess and check with a for loop, but thats caveman level stuff

Gotta learn proofs I guess.
Proofs definitely, but for now:

There's a function 'digits' that will tell you how many digits the nth fibonacci number has
There's another function that will spit out the index of the first fibonacci number with n digits
In the simplest case (you know each digit up to 1000) -> that's just a bunch of if statments
But elsewise you can derive the underlying mathematical relationship, and turn that into an explicit function.
Start with that recurrence relation and rules you picked up.
If that (simple) rule held, the function would simply be 'if n <= 5 return ... else return n * 5' 
with those extra rules it's with an elif for n % 19 ... etc.

data:
|f7| = 2
|f12| = 3
|f17| = 4
|f21| = 5
|f26| = 6
|f31| = 7
|f36| = 8
|f40| = 9
|f45| = 10
|f55| = 12
|f60| = 13
|f142| = 30
|f639| = 134

My next question is, if I have a random number n, there's no explicit mapping to the fibonacci numbers from that, I can't quite word this 
how I'd like, but it seems like I'm missing out on if the mapping is 1 way or 2 way, as I can't derive a fibonacci number without calculating it...
circular. 

alternative function, "given the index of a fibonacci number, derive it's magnitutde without calculating the number itself."
"""

def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

def digits(n):
    return len(str(fib(n)))

# index -> given a number n, return the index of the first fibonacci number with that many digits
def index(n):
    pass

"""
Using chatgpt;
We have an explicit formula for fibonacci numbers using Binet's formula F(n) will give us the nth fibonacci number.
Using the properties of logarithms the number of digits in a number can be calculated with another formula we'll call d(n).
Thus by composing the two, we have a formula we'll call DFib that calculated d(F(n)) => thus giving us the digits of the nth fibonacci number.
For a fibonacci number to have at least 'd' digits we need DFib(n) >= d-1 
Then, by writing out the (approximmation) of our formula and solving for n we are left with the explicit formula to solve for the index 'n' of the first fibonacci number with 'd' digits.
we'll call it iDFib(d) -> n
---
So looking back to today and yesterday's work; I was sure this was going to need some crazyness with proofs I had long forgotten about.
But I forget something even more bedrock in mathematics; setting up an equation to solve for the number you want.
This was facilitated by not stopping to look a little deeper into fibonacci numbers.
"""

phi = (1 + sqrt(5)) / 2
psi = 1 - phi

def F(n):
    return int((phi**n - (1 - phi)**n) // sqrt(5))

def d(n):
    return floor(log10(n)) + 1

def iDFib(d):
    num = (d-1) + log10(sqrt(5))
    denom = log10(phi)
    n = ceil(num / denom)
    return n

# close as we're gonna get ~ 4781
print(iDFib(1000))

"""
Next time, maybe look into studying some basic fundamentals, pen and paper stuff. Sounds satisfying. Like doing mental pushups.
---
Lastly, your instincts told you precisely that's why and where you wanted 'ceil', dummy. Slow down to look at your output next time.
"""
