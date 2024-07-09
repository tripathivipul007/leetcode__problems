class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums)==1:
            return True
        
        
        maxreach = 0
        
        for i in range(len(nums)-1):
            if i> maxreach:
                return False
            
            maxreach = max(maxreach, i+nums[i])
            if maxreach>= len(nums)-1:
                return True
            
        return False
        
        
        