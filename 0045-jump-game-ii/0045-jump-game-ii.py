class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0   
        
        jumps = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                jumps += 1
                currentEnd = farthest

                if currentEnd >= len(nums) - 1:
                    break
        
        return jumps
