class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        numbers= {} #key is number, value is index
        for i, num in enumerate(nums):
            difference = target - num #establish a difference
            if difference in numbers:
                return [numbers[difference], i]
            else:
                numbers[num] = i

                #for python, its always dict[key] = value


        
        
        # numbers = {} #key is number, and value is index
        # for i, num in enumerate(nums): #iterating through list with storing the index too
        #     difference = target - num #getting difference
        #     if difference in numbers: #if difference is in numbers,
        #         return [numbers[difference], i] #return the index of difference and index of current number
        #     else:
        #         numbers[num] = i #if not, add the current number as the key and its index the value to the dictionary

#time complexity: O(n) because one for loop 
#space complexity: O(1) because one dictionary created

#how can we make this slower


        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        
#         #setting up the function and indicating that the function expects numbers in a list and the target value is an int that comes from the list
#         num_map = {} #this is the hash table to store a number and its index
#         for i, num in enumerate(nums): #enumerate helps you go through the list
#             difference = target - num #finding the difference that you need to look for in the hash map
#             if difference in num_map: #conditional statement asking if difference is contained in the hash map,
#                 return [num_map[difference], i] #returning the indexes of the two identified values
#             num_map[num] = i #storing the number with its index

# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         num_map = {}  # Hash table to store number and its index
# #         for i, num in enumerate(nums):
# #             complement = target - num  # Find the complement
# #             if complement in num_map:
# #                 return [num_map[complement], i]  # Return indices of complement and current number
# #             num_map[num] = i  # Store the number with its index
