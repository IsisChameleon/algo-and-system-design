8. Implement the Fibonacci algorithm in three different methods: 
1. recursively, 
2. iteratively, and 
3. using memoization.

The Fibonacci sequence is a classic problem in software engineering interviews. 
Atlassian needs to implement scalable solutions, and your approach to this problem will reveal how well you understand this.

How to Answer
Demonstrate your understanding of the trade-offs between simplicity (recursion), efficiency (iteration), and optimization (memoization). Explain how each approach can be used in different scenarios based on computational resources and execution time.
Example
“A recursive solution involves a function calling itself with a smaller subset of the problem until it reaches a base case. This method is straightforward but can lead to significant inefficiencies due to repeated calculations. The iterative approach calculates each Fibonacci number sequentially, starting from the base cases and building up to the desired number by looping from 0 to n. This method is more efficient as it doesn’t involve repeated calculations or deep call stacks. Memoization optimizes the recursive solution by storing previously calculated Fibonacci numbers in a data structure during the function’s execution. When the function is called again with the same input, it first checks if the result is in the storage to avoid recalculating, thus reducing the number of computations needed.”

# Memoization (Isabelle == caching results)

Memoization is a technique used to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. For the Fibonacci sequence,          
memoization can be applied to both the recursive and iterative methods, but it is most commonly used with recursion to avoid the exponential time complexity caused by redundant calculations.                          

Here's how memoization works with the recursive method:                                                                                                                                                                 

 1 Create a dictionary (or any other form of cache) to store Fibonacci numbers as they are calculated.                                                                                                                  
 2 When the getFibonacci_recursion function is called, first check if the result for the current n is already in the cache.                                                                                             
 3 If it is, return the cached result instead of performing the recursive calculation.                                                                                                                                  
 4 If it is not, perform the calculation, store the result in the cache, and then return the result.                                                                                                                    

This approach turns the exponential time complexity of the naive recursive solution into linear time complexity, as each Fibonacci number is calculated only once.    
