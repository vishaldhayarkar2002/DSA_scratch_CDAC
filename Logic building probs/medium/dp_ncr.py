# Python implementation to find 
# Binomial Coefficient using memoization

def getnCk(n, k, memo):
  
    # k cannot be greater than n so we return 0 here
    if k > n:
        return 0
    
    # base condition when k and n are equal or k = 0
    if k == 0 or k == n:
        return 1
    
    # Check if pair n and k is already 
    # calculated then return it from here
    if memo[n][k] != -1:
        return memo[n][k]
    
    # Recursive add the value and store to memo table
    memo[n][k] = getnCk(n - 1, k - 1, memo) + \
    getnCk(n - 1, k, memo)
    return memo[n][k]

def binomialCoeff(n, k):
  
    # Create table for memoization
    memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)] 
    # This is important more
    
    return getnCk(n, k, memo)

n, k = 5, 2
print(binomialCoeff(n, k))