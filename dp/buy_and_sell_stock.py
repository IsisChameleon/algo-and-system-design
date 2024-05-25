"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
"""

from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    
    n = len(prices)
    dp_free = [0]*n 
    dp_hold = [0]*n 
    
    dp_free[0] = 0
    dp_hold[0] = -prices[0]  #at time of the only way to hold the stock is to buy it

    for i in range(1, n):
        print(f'Iteration {i}: {prices[i]}')

        dp_hold[i] = max(dp_free[i-1] - prices[i], dp_hold[i-1]) # to hold the stock on i, we either have no stock and buy it, or we hold the stock from before
        dp_free[i] = max(dp_hold[i-1] + prices[i] - fee, dp_free[i-1]) # to be free of stock on i, we either have no stock and do nothing, or we have stock and sell it   
        print(f'...dp_hold[i] {dp_hold[i]}: max free-1+buy {dp_free[i-1] - prices[i]}, keep_holding {dp_hold[i-1]}')
        print(f'...dp_free[i] {dp_free[i]}: max hold-1+sell {dp_hold[i-1] + prices[i] - fee}, keep_free {dp_free[i-1]}')
    return max(dp_free[-1], dp_hold[-1])


"""
Complexity Analysis
Let nnn be the length of the input array prices.

Time complexity: O(n)O(n)O(n)

We iterate from day 1 to day n - 1, which contains n - 1 steps.
At each step, we update free[i] and hold[i] which takes O(1)O(1)O(1).
Space complexity: O(n)O(n)O(n)

We create two arrays of length n to record the maximum profit with two status on each day.
"""

