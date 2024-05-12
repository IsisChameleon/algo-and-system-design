from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    
    # assuming it starts at 0
    if n == 0:
        return 0

    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
