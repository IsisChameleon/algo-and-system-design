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

    fib = getFibonacci_loop(current, prev, current_index, n)
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