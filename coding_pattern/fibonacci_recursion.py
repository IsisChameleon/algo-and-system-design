def fibonacci(n: int) -> int:

    # Type checking and validation

    # assuming it starts at 0
    if n == 0:
        return 0

    
    if n == 1:
        return 1

    prev = 0
    current = 1
    current_index = 1

    # Initialize the cache with base cases
    cache = {0: 0, 1: 1}
    fib = getFibonacci_recursion_with_cache(current, prev, current_index, n, cache)
    return fib

def getFibonacci_recursion_with_cache(current: int, prev: int, iteration: int, n: int, cache: dict) -> int: 
    # Check if the value is already in the cache
    if iteration in cache:
        return cache[iteration]

    # If not, compute the value and add it to the cache
    if iteration + 1 < n:
        cache[iteration + 1] = getFibonacci_recursion_with_cache(current+prev, current, iteration+1, n, cache)
        return cache[iteration + 1]
    else:
        return current+prev
    return fib

def getFibonacci_loop(current: int, prev: int, iteration: int, n: int) -> int: 
    while iteration != n:
        old_current = current
        current = current+prev
        prev = old_current
        iteration+=1
    return current

def getFibonacci_recursion(current: int, prev: int, iteration: int, n: int) -> int: 

    if iteration + 1 < n:
        fib = getFibonacci_recursion(current+prev, current, iteration+1, n)
    else:
        fib = current+prev
    return fib