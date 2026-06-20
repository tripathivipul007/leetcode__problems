class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        
        i=0
        j,k = 0,0
        while j<len(nums1) and k<len(nums2):
            if nums1[j]<nums2[k]:
                merged.append(nums1[j]) 
                j+=1
                
            elif nums2[k]<nums1[j]:
                merged.append(nums2[k]) 
                k+=1
                
        while j<len(nums1):
            merged.append(nums1[j]) 
            
            j+=1
            
        while k<len(nums2):
            merged.append(nums2[k])
            
            k+=1
            
        if len(merged)%2!=0:
            return merged[len(merged)//2]
        
        else:
            rindex = len(merged)//2
            lindex = rindex-1
            return (merged[rindex] + merged[lindex])/2
            
            
            
                
        