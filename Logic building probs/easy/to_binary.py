def decToBinaryRec(n, binArr):
    # Base Case
    if n == 0:
        return
    
    # Recur for smaller bits.
    decToBinaryRec(n // 2, binArr)
    
    # Add MSB of current number to the binary list
    binArr.append(str(n % 2))

# Function to convert decimal to binary
def decToBinary(n):
    if n == 0:
        return "0"

    binArr = []
    decToBinaryRec(n, binArr)
    return "".join(binArr)

if __name__ == "__main__":
    n = 12
    print(decToBinary(n))

# inbuilt method
import math

def decToBinary(n):
	return bin(n)[2::]
  
if __name__ == "__main__":
    n = 12
    print(decToBinary(n))