In NLP, stop words are commonly used words like "a", "is", and "the". They are typically filtered out during processing. 

  

Implement a function that takes a string text and an integer k, and returns the list of words that occur in the text at least k times. 
The words must be returned in the order of their first occurrence in the text. 

  

Example 

text = "a mouse is smaller than a dog but a dog is stronger" ,k=2 
The list of stop words that occur at least k = 2 times is ["a", "is", "dog"]. "a" occurs 3 times, "is" and "dog" both occur 2 times.
No other word occurs at least 2 times. The answer is in order of first appearance in text. 

  

Function Description  

Complete the function stop_words in the editor below. 

  

stop_words has the following parameter(s): 

    string text: the input text. 

    int k: the threshold occurrence count for a word to be a stop word 

  

Returns 

     string[]: the list of stop words in order of their first occurrence 

  

Constraints 

text has at most 50000 characters. 

Every character in text is either an English lowercase letter or a space. 

text starts and ends with a letter. No two consecutive characters are spaces, i.e. text is a valid sentence. 

There will be at least one stop word in the text. 

1 ≤ k ≤ 18 