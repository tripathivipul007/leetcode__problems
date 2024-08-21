class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        
        for i in range(0,len(s)-1):
            temp = abs(ord(s[i]) - ord(s[i+1]))
            score += temp
            
        return score
        