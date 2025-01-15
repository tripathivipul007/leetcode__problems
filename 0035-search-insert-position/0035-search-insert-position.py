class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = int(start + (end-start)/2)

            if nums[mid] == target:
                return mid
            elif target>nums[mid]:
                start = mid+1

            elif target<nums[mid]:
                end = mid-1

        if target > nums[mid]:
            return mid+1
        else:
            return mid

        