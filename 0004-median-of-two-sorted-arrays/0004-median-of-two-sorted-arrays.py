from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        i = j = 0
        merged = []

        target = (n1 + n2) // 2 + 1

        while len(merged) < target:
            if i < n1 and j < n2:
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1

            elif i < n1:
                merged.append(nums1[i])
                i += 1

            else:
                merged.append(nums2[j])
                j += 1

        total = n1 + n2

        if total % 2 == 1:
            return float(merged[-1])
        else:
            return (merged[-1] + merged[-2]) / 2.0