Q6. Quick Sort
https://www.ambitionbox.com/interviews/atlassian-question/quick-sort-you-are-given-an-array-of-integers-you-need-to-sort-the-array-in-ascending-order-using-quick-sort-quick-sort-is-a-divide-and-conquer-algorithm-in-which-we-choose-a-jqZ7wQ2X

You are given an array of integers. You need to sort the array in ascending order using quick sort.
Quick sort is a divide and conquer algorithm in which we choose a pivot point and partition the array into two parts i.e, left and right. The left part contains the numbers smaller than the pivot element and the right part contains the numbers larger than the pivot element. Then we recursively sort the left and right parts of the array.
Example:
Let the array = [ 4, 2, 1, 5, 3 ] Let pivot to be the rightmost number.

After the 1st level partitioning the array will be { 2, 1, 3, 4, 5 } as 3 was the pivot. After 2nd level partitioning the array will be { 1, 2, 3, 4, 5 } as 1 was the pivot for the left part and 5 was the pivot for the right part. Now our array is sorted and there is no need to divide it again.
Input format:
The first line of input contains an integer 'T' denoting the number of queries or test cases. The first line of each input consists of an integer 'N' denoting the size of the array. The second line of each input consists of 'N' space-separated integers denoting the elements of the array.
Output format:
For each test case, print a single line containing space-separated integers denoting the elements of the array after sorting. The output of each test case will be printed in a separate line.
Note:
You do not need to print anything, it has already been taken care of. Just implement the given function.
Follow Up
Can you solve this in the worst case NlogN complexity?
Constraints:
1 <= T <= 10 1 <= N <= 10 ^ 3 -10 ^ 9 <= ARR[i] <= 10 ^ 9 Where 'T' is the number of test cases, 'N' is the length of the array 'ARR', and 'ARR[i]' is the array element at index i. Time limit: 1 sec.

----------------------------------------------------------------------

Sure, here is an implementation of the Quick Sort algorithm in Python, along with comments explaining each part of the code and the time and space complexity analysis:

```python
def quicksort(arr):
    # Helper function to perform the partitioning
    def partition(low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]
        i = low - 1  # Pointer for the greater element
        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
                # Swapping element at i with element at j
                arr[i], arr[j] = arr[j], arr[i]
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        # Return the position from where partition is done
        return i + 1

    # Helper function to perform quicksort
    def quick_sort_recursive(low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = partition(low, high)
            # Recursive call on the left of pivot
            quick_sort_recursive(low, pi - 1)
            # Recursive call on the right of pivot
            quick_sort_recursive(pi + 1, high)

    # Initial call to quicksort
    quick_sort_recursive(0, len(arr) - 1)

# Example usage
arr = [4, 2, 1, 5, 3]
quicksort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]
```

### Time Complexity:
- **Best Case**: O(n log n)
  - This occurs when the pivot element is always the middle element, leading to balanced partitions.
- **Average Case**: O(n log n)
  - This is the expected time complexity for a random array.
- **Worst Case**: O(n^2)
  - This occurs when the pivot element is always the smallest or largest element, leading to highly unbalanced partitions. This can be mitigated by using techniques like random pivot selection or the median-of-three method.

### Space Complexity:
- **O(log n)**
  - This is due to the recursive stack space used by the algorithm. In the best and average cases, the depth of the recursion tree is log n. In the worst case, the depth can be n, but this is rare with good pivot selection strategies.
