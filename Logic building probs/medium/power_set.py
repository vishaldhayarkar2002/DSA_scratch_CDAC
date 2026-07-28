# Python program to find the power set using
# binary representation of a number.

def allPossibleStrings(s):
    n = len(s)
    result = []

    # Iterate through all subsets (represented by 0 to 2^n - 1)
    for i in range(1 << n):   
        subset = ""
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset += s[j]
                
            # Add the subset to the result
        result.append(subset)   

    return result

 
if __name__ == "__main__":
    s = "abc"
    subsets = allPossibleStrings(s)
 
    for subset in subsets:
        print(subset)   