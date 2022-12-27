implement a a function that gets a string made of 3 types of brackets in the following hierarchy: ‘()’, ‘[]’, ‘{}’. 

The function should check if the string is legal. 

Return Value: 

0 if legal 

1 if illegal 

Legal is: 

Every bracket is being closed. 

You can’t close a bracket if another bracket was opened after it. 

Examples: 

Legal strings: 

{[()]} 

[{[[[(())]]]}] 

{[]{{()}}} 

NULL  

Not legal: 

{) 

{([)]} 