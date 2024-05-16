# Question

Goku and Dragon Balls

Goku has ‘N’ Dragon Balls. Each Dragon Ball is unique with the ith Dragon Ball having ‘i’ stars on it. 
For example, the first Dragon Ball has 1 star, the second Dragon Ball has 2 stars, and so on.
Goku gave a task to Gohan to arrange the ‘N’ Dragon Balls in a binary tree-like structure. While making the binary tree, he has to make sure that these conditions must be fulfilled:
The left subtree of any particular Dragon Ball ‘D’ will always contain Dragon Balls with the number of stars less than that of the Dragon Ball ‘D’. The right subtree of any particular Dragon Ball ‘D’ will always contain Dragon Ball's with the number of stars greater than that of the Dragon Ball ‘D’.
Can you find out how many structurally unique binary trees Gohan can make by fulfilling these conditions?

# Algorithm

From the given conditions it is clear that we have to find how many structurally unique binary search trees are possible.

 

To find the unique BSTs,  we define two functions:

 

A(i,N): It denotes the number of unique BSTs, with ‘i’ (1 <= ‘i’ <= N) as the root.

B(N): It denotes the number of unique BSTs for a sequence of length N (number of Dragon Balls).

 

Now, we construct B(N) by the sum of A(i, N) :

B(N) = A(1, N) + A(2, N) + … + A(N, N)

 

Notice that when we select ‘i’ as a root i.e. A(i, N), we have i - 1 nodes which can be used to form a left subtree and n - 1 nodes to form a right subtree.

A(i, N) = B(i - 1) * B(N - i)

 

Thus, A(i, N) can be calculated by the product of the number of unique BSTs with i - 1 nodes and the number of unique BSTs with N - i nodes. Uniqueness is guaranteed by the sizes of the left subtree and the right subtree.

 

Here is the algorithm :

 

If N is 0 or 1 then we return 1 because the number of unique BSTs with 0 nodes or 1 node is 1.
We initialize ‘sum’ to 0. ‘sum’ stores gokuAndDragonBalls(N).
We iterate form i = 1 to i = N and call the recursive function.
We update sum as sum += gokuAndDragonBalls(i - 1) * gokuAndDragonBalls(n - i).
Finally, we return the sum as our answer.
Space Complexity: O(n)Explanation:
O(N), where N denotes the number of Dragon Balls.

 

In the worst case, extra space is used by the recursion stack which can go up to a maximum depth of N. Hence the space complexity is O(N).

Time Complexity: O(n^n)Explanation:
O(N ^ N), where N denotes the number of Dragon Balls.

 

In the worst case at every step, we are making N recursive calls. For every ‘i’ (1 <= ‘i’ <= N)  we make two recursive calls i.e one is to find the number of unique BSTs with i - 1 nodes and the other is to find the number of unique BSTs with N - i nodes. So, the maximum depth of the recursion tree can go up to N. Hence the time complexity is O(N ^ N).