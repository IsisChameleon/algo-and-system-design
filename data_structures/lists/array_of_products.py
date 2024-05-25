def arrayOfProducts(array):
    
    N = len(array)
    print(f'Array {array} len {N}')
    if N==0:
        return 0
    if N==1:
        return 0
    left_mul = [1 for i in range(N)]
    right_mul = [1 for i in range(N)]
    mul = [1 for i in range(N)]
    
    # Write your code here.
    for i, value in enumerate(array):
        left_mul[i] = value * left_mul[i-1] if i-1 >= 0 else value

    for i in range(N-1, -1, -1): # e.g. 9, 8, 7, 6, ...0 for N=10
        right_mul[i] = array[i] * right_mul[i+1] if i+1 < N else array[i]

    print(f'{left_mul}, //, {right_mul}')

    for i in range(N):
        if i==0:
            mul[i] = right_mul[i+1]
        elif i==N-1:
            mul[i] = left_mul[i-1]
        else:
            mul[i] = left_mul[i-1]*right_mul[i+1]

    return mul

# passed algo expert