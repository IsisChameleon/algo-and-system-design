def quicksort(arr):
    """
    The partition function is a key part of the Quick Sort algorithm. 
    It rearranges the elements in the array such that all elements less than or equal 
    to the pivot are on the left of the pivot, and all elements greater than the pivot are on the right. 
    The pivot is chosen as the rightmost element in the current subarray.
    """
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