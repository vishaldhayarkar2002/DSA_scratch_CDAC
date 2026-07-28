# Check if string contains only 0s and 1s
def is_binary(s):
    return set(s) <= {'0', '1'}

# Examples
print(is_binary("101010"))  # Output: True
print(is_binary("101210"))  # Output: False

def is_binary_all(s):
    return all(char in '01' for char in s)

def is_binary_manual(s):
    if not s:  # Empty string
        return False
    for char in s:
        if char not in '01':
            return False
    return True

class SetProblems:
    
    @staticmethod
    def is_subset(arr1, arr2):
        return set(arr1).issubset(set(arr2))
    
    @staticmethod
    def are_disjoint(arr1, arr2):
        return set(arr1).isdisjoint(set(arr2))
    
    @staticmethod
    def union_arrays(arr1, arr2):
        return list(set(arr1) | set(arr2))
    
    @staticmethod
    def intersection_arrays(arr1, arr2):
        return list(set(arr1) & set(arr2))
    
    @staticmethod
    def has_pair_with_sum(arr, target):
        seen = set()
        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False
    
    @staticmethod
    def find_pair_with_sum(arr, target):
        seen = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None

# Test Cases
if __name__ == "__main__":
    sp = SetProblems()
    
    # Test subset
    print("Is Subset:", sp.is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
    
    # Test disjoint
    print("Are Disjoint:", sp.are_disjoint([1, 2, 3], [4, 5, 6]))
    print("Are Disjoint (overlap):", sp.are_disjoint([1, 2, 3], [3, 4, 5]))
    
    # Test union
    print("Union:", sp.union_arrays([1, 2, 3, 4], [3, 4, 5, 6]))a
    
    # Test intersection
    print("Intersection:", sp.intersection_arrays([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    
    # Test pair sum
    arr = [1, 4, 3, 5, 6]
    print("Has Pair Sum 10:", sp.has_pair_with_sum(arr, 10))
    print("Find Pair Sum 10:", sp.find_pair_with_sum(arr, 10))