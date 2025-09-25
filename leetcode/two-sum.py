class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: #setting up the function and indicating that the function expects numbers in a list and the target value is an int that comes from the list
        num_map = {} #this is the hash table to store a number and its index
        for i, num in enumerate(nums): #enumerate helps you go through the list
            difference = target - num #finding the difference that you need to look for in the hash map
            if difference in num_map: #conditional statement asking if difference is contained in the hash map,
                return [num_map[difference], i] #returning the indexes of the two identified values
            num_map[num] = i #storing the number with its index

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         num_map = {}  # Hash table to store number and its index
#         for i, num in enumerate(nums):
#             complement = target - num  # Find the complement
#             if complement in num_map:
#                 return [num_map[complement], i]  # Return indices of complement and current number
#             num_map[num] = i  # Store the number with its index