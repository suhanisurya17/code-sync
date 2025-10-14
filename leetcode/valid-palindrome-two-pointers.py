class Solution:
  def isPalindrome(self, s: str) -> bool:
    p = "".join(c.lower() for c in s if c.isalnum())
    left  = 0
    right = len(p) - 1

    while left < right:
      if p[left] != p[right]:
        return False
        break
      left+=1
      right -= 1
    return True
