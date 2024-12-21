class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct_indices = {}
        
        for i in range(len(nums)):
            if nums[i] in distinct_indices:
                if abs(distinct_indices[nums[i]] - i) <= k:
                    return True
                
                
            
               
            distinct_indices[nums[i]] = i
                    
        return False
                    