from collections import Counter

def topKFrequent_brute(nums, k):
    count = Counter(nums)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

# Time: O(n log n) — sorting
# Space: O(n)
# Heap  version ------------------------------------
import heapq
from collections import Counter

def topKFrequent_heap(nums, k):
    count = Counter(nums)

    # Min-heap of size k
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

# Bucket sortt version
from collections import Counter

def topKFrequent(nums, k):
    # Step 1: count frequencies
    count = Counter(nums)

    # Step 2: create buckets where index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    # Step 3: scan buckets from highest frequency
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result