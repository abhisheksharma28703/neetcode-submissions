class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        n = nums1 + nums2
        n.sort()
        total = len(n)
        if total % 2 != 0:
            return n[total//2]
        else:
            return (n[total//2]+n[(total//2)-1])/2