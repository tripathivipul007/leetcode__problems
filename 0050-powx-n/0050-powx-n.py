class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        
        # Handle negative exponent by converting it to positive and inverting the result
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x
        
        while n > 0:
            # If n is odd, multiply result by current product
            if n % 2 == 1:
                result *= current_product
            
            # Square the current product and halve the exponent
            current_product *= current_product
            n //= 2
        
        return result