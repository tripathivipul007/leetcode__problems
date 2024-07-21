class Solution:
    
    def calc(self, n: int)-> int:
        summ=0
        while n>0:
            temp = n%10
            summ += temp*temp
            n=n//10
        return summ
    
    def isHappy(self, n: int) -> bool:
        
        ledger = set()
        while n != 1 and n not in ledger:
            ledger.add(n)
            n = self.calc(n)
        return n == 1
            
            
        