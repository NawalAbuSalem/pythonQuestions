Given a chess board having N×N cells, you need to place N queens on the board in such a way that no queen attacks any other queen. 

Implement a function can_organize_the_board that takes 

Input: 

1.        board - The board of N×N cells 

2.        N - The number of queens to place 

Output: 
If it is possible to place all the N queens in such a way that no queen attacks another queen, then print "Yes" in first line, then print N lines having N integers. 
The integer in I’th line and j’th column will denote the cell (i,j) of the board and should be 1 if a queen is placed at (i,j) otherwise 0. If there are more than way of placing queens print any of them. 

If it is not possible to place all N queens in the desired way, then print "No" 

Constraints: 
1≤N≤10. 

  

For example: 

board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]  

N=4 

can_organize_the_board(board, N) 

Yes 

0 1 0 0  

0 0 0 1  

1 0 0 0  

0 0 1 0 

  

board = [[0,0,0], [0,0,0], [0,0,0]] 

N=3 

can_organize_the_board(board, N) 

No 