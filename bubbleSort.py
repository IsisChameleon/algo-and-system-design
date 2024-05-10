def bubbleSort(array):
    # Write your code here.
    end = len(array)-1
    sorted_array = bubbleSortIt(array, end)
    return sorted_array

# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSortIt(array, end):
    nb_swaps = 0
    print(f'array {array} end {end}')
    for i in range(1, end+1):
        if array[i-1] > array[i]:
            nb_swaps+=1
            
            smaller = array[i]
            array[i]=array[i-1]
            array[i-1]=smaller
    print(f'array {array} end {end} nb_swaps {nb_swaps}')
    if nb_swaps == 0:
        return array
    else:
        end-=1
        return bubbleSortIt(array, end)