class Solution:
    def romanToInt(self, s: str) -> int:
        roman2integer = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        ans =0
        prev_val=0
        
        for i in range(len(s)-1, -1, -1):
            currval = roman2integer[s[i]]
            
            if currval<prev_val:
                ans-=currval
            else:
                ans+=currval
                
            prev_val = currval
        
        return ans
            
        
              
            
        