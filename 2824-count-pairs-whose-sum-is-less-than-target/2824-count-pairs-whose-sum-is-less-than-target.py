class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n =len(nums)
        counter = 0
        
        for i in range(n):
            for j in range(n):
                if i<j and nums[i] +nums[j] < target:
                    counter+=1
                    
        return counter
            