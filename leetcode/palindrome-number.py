class Solution:
    def isPalindrome(self, x: int) -> bool:
        xcomparison = x
        reverse = 0 #starter value

        if x < 0:
            return False

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcomparison