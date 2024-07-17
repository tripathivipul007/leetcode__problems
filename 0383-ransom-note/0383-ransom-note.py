class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_magazine={}
        
        for i  in range(0,len(magazine)):
            temp=magazine[i]
            if temp not in counter_magazine:
                counter_magazine[temp]=1
            else:
                counter_magazine[temp]+=1
                    
        for i in range(0,len(ransomNote)):
            temp = ransomNote[i]
            if temp not in counter_magazine:
                return False
            else:
                counter_magazine[temp]-=1
                if counter_magazine[temp]<0:
                    return False
        return True
                    
                    
                    
                    
        
            