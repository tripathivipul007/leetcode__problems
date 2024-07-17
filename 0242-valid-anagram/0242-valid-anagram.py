class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counter ={}
        
        for i in range(0, len(s)):
            
            if s[i] not in counter:
                counter[s[i]]=1
            else:
                counter[s[i]]+=1
        
        for i in range(0, len(t)):
            
            if t[i] not in counter:
                return False
            
            counter[t[i]] -=1
            
            if counter[t[i]]<0:
                return False
        
        return True
        