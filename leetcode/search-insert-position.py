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
