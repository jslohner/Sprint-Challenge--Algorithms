#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I would say that for this function, the runtime complexity is: Logarithmic - O(log n)
I think that this is the case because as (n) increases, time taken to complete the program grows at a slightly slower rate.
As (n) increases the amount of loops increases as well, but not at a fast rate, for example if (n = 3) there will be 3 loops
and if (n = 5) there will be 5 loops.

b) For this function I think the runtime complexity is: Linearithmic - O(n log n)
I think for this function as (n) increases, time taken to complete it grows at a slightly faster rate. This is because as (n)
increases, the longer it takes for the while loop condition to be met. For example if (n = 3) after run - (sum = 6) because
for each iteration of the for loop, there are 2 iterations of the while loop. If (n = 5) after run - (sum = 15) because for
each iteration of the for loop in this case, there are 3 iterations of the while loop. As (n) increases not only do the for
loop iterations increase, the while loop iterations increase as well.

c) For this function I think the runtime complexity is: Linear - O(n)
For this function as (n) increases the runtime grows at the same rate. This is because as (n) increases the amount of recursions
will also increase, but there will always be (n - 1) recursions, so the function will take longer but only as long as (n). For
example if (n = 5) there will be (n - 1) recursions - 4 recursions. If (n = 10) there will be - 9 recursions. This will always
be the case no matter how big (n) is.

## Exercise II
For this solution I decided to start at the (bottom floor) and increment current floor until the dropped egg breaks using a while loop.
I would say that for this solution the runtime complexity is: Linear - O(n). This is because as input increases, runtime increases at
the same rate.

(n) = story

## initialize (floor) variable
floor = 0
## initialize (current) variable
current = 0
## initialize (search) boolean
search = True
## write while loop with condition search being true
while search:
##	increment current floor
	current += 1
##	check if egg breaks at current
	if egg breaks at current:
##		change search to false and floor to current
		search = False
		floor = current
## return floor that eggs break at
return floor
