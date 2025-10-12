class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()  # creating empty hash set
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.add(num)  # must add value to hash set
        return False