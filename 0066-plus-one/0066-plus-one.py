class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-1] = 0
            i = -2
            while i >= -len(digits) and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i < -len(digits):  # If all digits are 9
                digits.insert(0, 1)
            else:
                digits[i] += 1
        else:
            digits[-1] += 1
            
        return digits
        