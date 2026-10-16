import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    reverse_heap = []
    result = []
    heapq.heapify(nums)

    for num in nums:
        heapq.heappush(reverse_heap, -num)
    
    while reverse_heap:
        top = -heapq.heappop(reverse_heap)
        result.append(top)
    return result


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
