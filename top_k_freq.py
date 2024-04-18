from typing import List
from collections import defaultdict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count the frequency of each element
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1
    
    # Step 2: Create a list of buckets to store elements with the same frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Step 3: Get the top k frequent elements
    top_k = []
    for bucket in reversed(buckets):
        top_k.extend(bucket)
        if len(top_k) >= k:
            break
    
    return top_k

arr = [1,1,1,2,2,3,2,3,4,1,2,5,5,5,5,5,5]
print(topKFrequent(arr,2))