class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        reverse=""
        substring=""
        for i in range(len(s)-1, -1, -1):
            if s[i]==" ":
                if substring:
                    tempsub=substring[::-1]
                    reverse = reverse + tempsub+ " "
                    substring = ""
                
            else:
                substring+=s[i]
        if substring:     
            tempsub=substring[::-1]
            reverse = reverse + tempsub   
            
                
        return reverse
            
                
            
            