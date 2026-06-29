class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        nums3 = []

        while i < m and j < n:
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < m:
            nums3.append(nums1[i])
            i += 1
        while j < n:
            nums3.append(nums2[j])
            j += 1
        total = len(nums3)
        if total % 2 != 0:
            return nums3[total//2]
        else:
            return (nums3[total//2]+nums3[(total//2)-1])/2
        