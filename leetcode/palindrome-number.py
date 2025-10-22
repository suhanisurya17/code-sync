class Solution:
    def isPalindrome(self, x: int) -> bool:
        #two pointer method: must turn int into string
        x1 = str(x)
        left = 0
        right = len(x1) - 1
        while left < right:
            if x1[left] != x1[right]:
                return False
            else:
                left+=1
                right-=1
        return True


        # method of not turning into a string
        x2 = x
        reverse = 0 #starts off at zero before extracting digits

        #edge case 1, x is a negative number
        if x < 0:
            return False
        
        #getting into digit extraction
        #using while loop because we don't know how many digits
        while x > 0:
            reverse = (reverse * 10) + (x % 10) #recursive action to extract digits
            x //= 10 #updating x after every digit is extracted

        return x2 == reverse #returning if the reverse digit extracted number is the same as the original
        
        #code tracing
        # x = 121
        # x_copy = 121
        # reverse = 0 + (121 % 10) = 1
        # x = 12
        # reverse = 10 + (12 & 10) = 10 + 2 = 12
        # x = 1
        # reverse = 120 + (1 % 10) = 120 + 1
        # x = 0, loop stops
    
