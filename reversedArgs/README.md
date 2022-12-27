Given an arbitrary function, return a new function, which when called, returns the result of the original function called with the arguments in reversed order. 

  

For example, if the original function, f, is a pow function, f(2,3) = 8, 23 = 8, then the correct result is a function g, with g(3,2) = 9, because 32 = 9.
Complete the function described below. Your function will be tested on 4 different functions included in the locked template code. 

  

Function Description  

  

Complete the function reversed_args in the editor below. 
The function must return a new function g which, when called, returns the result of f called with the arguments reversed. 

  

reversed_args has the following parameter(s): 

    f: the function whose result needs to be computed with the order of arguments reversed. 

  

Constraints 

1 ≤ q ≤ 100 

None of the functions will be called with more than 100 arguments. 

The length of every string argument is at most 10. 