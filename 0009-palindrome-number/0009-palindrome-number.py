class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        rev = number[::-1]
        if rev == number:
            return True
        else:
            return False
            
            
        