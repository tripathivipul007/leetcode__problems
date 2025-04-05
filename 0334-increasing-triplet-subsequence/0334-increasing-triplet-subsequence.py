class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # new smallest
            elif num <= second:
                second = num  # new second smallest
            else:
                # Found a number > second => triplet exists
                return True

        return False
