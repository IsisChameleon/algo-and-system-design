"""
Maximum Subarray Sum
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be -1.
"""

from typing import List


def max_subarray_sum(arr: List[int]) -> int:

    # base case
    max_ending_at_i = global_max = arr[0]

    # iterate through the array
    for i in range(1, len(arr)):
        max_ending_at_i = max(arr[i], max_ending_at_i + arr[i]) # we either take the element alone or with the previous sum
        global_max = max(global_max, max_ending_at_i)
    return global_max

"""
[-5, -1, -8, -9]
-5 -5
-1 or -5 -1 => -1 => global max -1
-8 or -1 -8 => -1 => global max -1
-9 or -1 -9 => -1 => global max -1

"""