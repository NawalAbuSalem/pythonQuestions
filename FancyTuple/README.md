Implement the class FancyTuple. 

1. The constructor takes 0 to 5 parameters. 

2. The elements of FancyTuple can be accessed as named properties: first, second, third, fourth, and fifth. 
The expression FancyTuple("dog", "cat").first returns "dog" and FancyTuple("dog", "cat").second returns "cat". 

3. An AttributeError exception is raised if a nonexistent element of the tuple is accessed. 
The expression FancyTuple("dog", "cat").third raises an AttributeError exception. 

4. len(FancyTuple) returns the number of elements. len(FancyTuple("dog", "cat")) returns 2. 

  

Your implementations of the class will be tested by a provided code stub on several input files. 
Each input file contains parameters to tests your implementation with. First, the provided code stub initializes the instance of FancyTuple.
Next, it tests the implementation by accessing its elements and checking its length. 
The result of their executions will be printed to the standard output by the provided code. 