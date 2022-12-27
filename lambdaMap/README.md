The square operation is to be performed on an input array of arrays. It is to be applied only to the integers which are greater than 0, 
ignoring the rest, i.e., the rest are not to be included in the output. The input is not exactly a 2D array as all the rows can have
 a different number of elements. Fill in the required lambda function to achieve this in the editor below. 

  

Take, for example, the input array be arr = [[-1, 1, 2, -2, 6], [3, 4, -5]], 
of length n = 2. First remove the elements less than or equal to 0 to get arr' = [[1, 2, 6], [3, 4]]. 
Then, squaring each element, the result is [[1, 4, 36], [9, 16]]. 

  

Function Description 

Complete the function lambdaMap in the editor below. 
Write the Lambda function required to achieve this. 

  

lambdaMap has the following parameters: 

    arr[arr[0], ..., arr[n-1]]: an array of arrays 

  

Constraints 

1 ≤ n ≤ 104 

1 ≤ |arr[i]| ≤ 10 

-104 ≤ arr[i] ≤ 104 (where 0 ≤ i < n) 