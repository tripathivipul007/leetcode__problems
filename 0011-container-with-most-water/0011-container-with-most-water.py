class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        left=0
        right = n-1
        maxwater = 0
        
        while left<right:
            currwater = min(height[left],height[right])*(right-left)
            
            maxwater = max(currwater, maxwater)
            
            if height[left]<height[right]:
                left+=1
                
            else:
                right-=1
                
        return maxwater
            
            
            