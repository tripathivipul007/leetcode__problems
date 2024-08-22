class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        l_count = 0
        r_count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l_count +=1
            elif s[i] =='R':
                r_count +=1
            if l_count == r_count:
                counter +=1
                l_count = 0
                r_count = 0
                
        return counter
            
                
        
        