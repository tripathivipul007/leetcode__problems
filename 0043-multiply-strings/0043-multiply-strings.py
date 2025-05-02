class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2=='0':
            return '0'
        num1int = 0
        num2int = 0
        temp = 1
        for alpha in num1[::-1]:
            
            num1int+= int(alpha)*temp
            temp*=10

        temp2 = 1
        for alpha in num2[::-1]:
            
            num2int+= int(alpha)*temp2
            temp2*=10

        return str(num1int*num2int)

        