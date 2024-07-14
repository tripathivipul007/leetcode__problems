import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_string = re.sub(r'[^a-z0-9]','',s.lower())
        length = len(clear_string)
        
        
        for i in range(length//2):
                if clear_string[i] != clear_string[length-1-i]:
                    return False
        return True
                    
        