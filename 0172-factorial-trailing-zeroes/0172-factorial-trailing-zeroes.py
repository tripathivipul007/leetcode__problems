class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n==0 or n==1:
                return 1
            else:
                return fact(n-1)*n
            
        ans = fact(n)
        counter = 0
        while ans %10 ==0:
            counter +=1
            ans = ans//10
        return counter
        