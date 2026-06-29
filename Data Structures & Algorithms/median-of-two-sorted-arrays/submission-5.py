class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        idx1 = (m+n)//2
        idx2 = idx1-1
        i = 0
        j = 0
        ind1el = -1
        ind2el = -1
        cnt = 0
        while i<m and j<n :
            if nums1[i]<nums2[j]:
                if cnt == idx1: ind1el = nums1[i]
                if cnt == idx2: ind2el = nums1[i]
                i += 1
                cnt += 1
            else :
                if cnt == idx1: ind1el = nums2[j]
                if cnt == idx2: ind2el = nums2[j]
                j += 1
                cnt += 1
        while i<m:
                if cnt == idx1: ind1el = nums1[i]
                if cnt == idx2: ind2el = nums1[i]
                i += 1
                cnt += 1
        while j<n:
                if cnt == idx1: ind1el = nums2[j]
                if cnt == idx2: ind2el = nums2[j]
                j += 1
                cnt += 1
        if (m+n)%2!=0:
            return ind1el
        else :
            return (ind2el+ind1el)/2



