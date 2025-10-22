def binary_sort(nums, target):
        position = bisect.bisect_left(nums) #this is where the target value would go
        if position == 0: #if target is the smallest element, it would return say put it at index 0
            return nums[0]
        if position == len(nums):#if the target is the largest element, it would say put it at the last index
            return nums[-1]
        before = nums[position - 1] #this is the element before insertion point
        after = nums[position] #this is the element at the current insertion point
        return before if abs(before - target) <= abs(after - target) else after 
        #return which ever one is closer to the target
