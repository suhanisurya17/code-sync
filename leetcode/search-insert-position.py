#more inefficient solution O(n) time complexity
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #super simple question with case handling
      #case 1: the number is present in the list  
      if target in nums:
            return nums.index(target)            
      #else, it will start a counter and iterate through each value and be placed after it  
      else:
            counter = 0
            for num in nums:
                if target > num:
                    counter += 1
            return counter

#more efficient solution harnessing the power of binary sort

class Solution:
    import bisect
    def searchInsert(self, nums:List[int], target:int) -> int:
        if target in nums:
            return nums.index(target)
        else: #this part does the binary sort algorithm
            return bisect.bisect_left(nums, target)
