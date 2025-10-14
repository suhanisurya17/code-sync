class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "" #empty string at first
        for char in s: #checking if it is an actual character or not
            if char.isalnum():
                cleaned+= char.lower()
        return cleaned == cleaned[::-1] #comparing cleaned to its reverse
