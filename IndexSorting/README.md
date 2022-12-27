An array of arrays needs to be sorted on one or more columns. There is a list of [index to sort on, descending = 1||ascending = 0] pairs provided. 
Complete the lambda function to perform the requested sorts. 

  

Example 

arr = [[1, 2, 1], [3, 3, 1], [4, 2, 3], [6, 4, 3]] 

indices = [[1, 0], [2, 1]] 

  

The primary sort key is column 1, ascending. This sort produces [[1, 2, 1], [4, 2, 3], [3, 3, 1], [6, 4, 3]]. The column 1 values are 2, 2, 3, 4. 

The secondary sort key is column 2, descending. This applies to the two records that tied in the primary sort: [1, 2, 1] and [4, 2, 3]. These are sorted descending as [4, 2, 3], [1, 2, 1] using column 2 values 3, 1. 

The sorted list is [[4, 2, 3], [1, 2, 1], [3, 3, 1], [6, 4, 3]] 

  

NOTE: The sort should be stable, i.e. in the event of a tie, the array that is at the lower index originally is at the lower index in the result. 
See the first sort above where there is a tie between the 2s. [1, 2, 1] came before [4, 2, 3] in the original array. 

  

Functions Description 

Complete the lambda expressing in the indexSort function below. 

indexSort has the following parameters: 

    arr[n][m]: a 2-dimensional array of arrays of size m 

    indices[k][2]: a 2-dimensional array of 2 element arrays: [sort index, direction] 

  

Returns 

    None: The lambda function sorts the global array in place. 

  

Constraints 

1 ≤ n ≤ 104 

1 ≤ m ≤ 10 

1 ≤ k ≤ m 

0 ≤ indices[i][0] < m (where 0 ≤ i < k) 

indices[i][1] is either 0 or 1 

0 ≤ arr[i][j] ≤ 109 (where 0 ≤ i < n, 0 ≤ j < m) 