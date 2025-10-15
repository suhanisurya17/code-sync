class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # Sort by frequency and take top k
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Extract just the numbers (not frequencies)
        result = [num for num, freq in sorted_items[:k]]
        
        return result
