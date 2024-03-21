2 spaces per num + 1 white space per (row num -2)



"Iteration rule"

Starting from L*15 (left most path) what we want is to flip 1 segment along the path to R each iteration of a loop
No more or less.

Evantually getting all the way to R*15

Flipping 1 node each iteration; 

Say we have all Ls on the first iter, and no flips
Increment a counter?

Next iter, we flip the first node according to the counter, the rest Ls

And do on.
That will get us all the paths with one R, 
--- 
To iterate through the tree we can go with a double for loop, and counter on the range of the inner loop for size
---
Each time count goes up, let's change the position we add the R along the path.
---
Now we want to add a second R along our path, which needs to vary in spacing to the first R. So if R1 is at the last position, we need R2 to vary in position from start to finish, skipping R1? Or just ignoring it.
This makes me think of having another loop, for every R1 in a sense, or recursion. 
---x
Every 15 iterations of the outmost loop we add an R (discounting the first)
---
Let's just say
Let's just say:
We have a bool list of length 15 called 'flip'
everytime the i loop runs, we flip 1 val
The trick is, how do we know which 1 to flip?
Naturally we'll need a counter variable, but this is quickly turning into counter hell.
There is an 'iteration rule' to follow for it
aaaaand I just remembered how binary strings work.
---
Take an input the binary string and the tree





