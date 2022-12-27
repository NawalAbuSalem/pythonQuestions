n this problem, we need to implement an improvement over the Python map generator. 
The map generator takes the input of a function (f) and an iterable (input) and returns an iterable (output) where outputi is f(inputi). 

  

In this problem, you have to implement a custom map generator, where instead of one function, you need to map a series of functions over an input. 
So, to the custom map generator, the inputs will be a list of functions and the list of integers over which all the functions are to be mapped one by one. 

  

Take for example, we have functions given as funcs = [lambda x: x*x, lambda x: x+x], with size n = 2. 
The first function is the "square" function and second function is the "double" function. Let the given input be arr = [1, 2, 3, 4] with size m = 4, 
then the output should be [2, 8, 18, 32], calculated as outputi = yi+yi, yi = arri*arri. 

  

Function Description 

Complete the function cmap in the editor below. The function must be a generator and should return an iterable. 

cmap has the following parameter(s): 

    funcs[funcs[0],...funcs[n-1]]:  an array of functions 

    arr[arr[0],...arr[m-1]]:  an array of integers 

  

Constraints 

1 ≤ n ≤ 10 

1 ≤ m ≤ 104 

funcsi is a callable function (where 0 ≤ i < n) 

0 ≤ arri ≤ 105 (where 0 ≤ i < m) 