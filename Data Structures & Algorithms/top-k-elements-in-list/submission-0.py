class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for i in nums:
            temp[i] = temp.get(i,0)+1
        temp_new = dict(sorted(temp.items(),key = lambda x:x[1],reverse=True))
        sorted_keys =list(temp_new.keys())
        ans = []
        for i in range(k):
            ans.append(sorted_keys[i])
        return ans
            