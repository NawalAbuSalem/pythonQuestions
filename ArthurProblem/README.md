Arthur needs to perform 3 operations on an input - squaring a number, taking the square root of a number or sum of the input numbers. 
But the order of these operations is not known beforehand. Arthur realizes it to be a perfect situation to implement it using 
co-routines and producer-filter-consumer pattern. 

Arthur has implemented the producer, consumer, and the pipeline and needs help to set up the accumulator (for summing the input), 
squarer (for squaring the input), and rooter (for taking the square root of a number) co-routines. 

1. The accumulator should receive one number, should add that to the previously kept answer, and yield that answer. The accumulator starts at 0. 

2. The squarer should receive one number and yield the square of that number. 

3. The rooter should receive one number and yield the square root of that number. 
Note that you need to take the floor after doing the square root of the input. 

  

Take, for example, the order in which to implement these functions to be order = [square, accumulate] and the numbers to be nums = [1, 2, 3] with length n = 3.
The complete function then is accumulate(square(numsi)). After the first number (1), the output is 1. After the second number (2), the output is 5.
After the third number (3), the output is 14. 

  

Functions Description 

Complete the co-routine accumulator, squarer, and rooter in the editor below. 

These co-routines do not have any input and communicate completely through the sub-routine pipeline. 

  

Constraints 

1 ≤ n ≤ 105 

1 ≤ numsi ≤ 105 (where 0 ≤ i < n) 