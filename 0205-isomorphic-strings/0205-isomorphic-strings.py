class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        match={}
        for i in range(0,len(s)):
            temp=s[i]
            if temp not in match:
                if  t[i] not in match.values():
                    match[temp]=t[i]
                else:
                    return False
            
            else:
                if match[temp] != t[i]:
                    return False
        return True
                
        