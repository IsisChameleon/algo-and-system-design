'''
Time complexity: O(N ^ 2)
Space complexity: O(N)

where N denotes the length of the sequence of integer to sort in a BST (1..N)
'''


mod = 1000000007

# let's calculate the sum of possible unique BST
# Consider that for a sequence of length N, the number of unique BST B(N) = sum (A(i, N)) for i = 1..N
# where A(i, N) is the number of BSTs with root i
# We also see that A(i, N) means there is i-1 nodes to the left forming a BST and N-i nodes to the right forming a BST
# ==> A(i, N) = B(i-1)*B(N-i)
# ==> B(N) = sum (A(i, N)) for i = 1..N = sum(B(i-1)*B(N-i)) for i =  1..N


def B(N: int, memo: list[int]) -> int:

    # if we have a sequence of length 0 or 1 there's only 1 BST

    if(N == 0 or N == 1):
        return 1
    
    # if we have already calculated the number of BSTs for that sequence N, let's find it in the cache

    if(memo[N] != -1):
        return memo[N] % mod

    sum = 0

    # B(N) =  sum(B(i-1)*B(N-i)) for i =  1..N

    for i in range(1, N + 1):
        sum += ((B(i - 1, memo) % mod) * (B(N - i, memo) % mod)) % mod

    memo[N] = sum % mod

    return memo[N]


def find_number_of_unique_bsts_for_sequence(N):

    # Initialize the calculation cache with -1

    memo = [-1] * (N + 1)  # we need 0, 1, ... N ==> N+1 spaces

    return (B(memo , N) % mod)