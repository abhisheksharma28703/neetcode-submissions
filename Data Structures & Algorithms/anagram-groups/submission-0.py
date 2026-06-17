
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sorted_word = ''.join(sorted(i))
            ans[sorted_word].append(i)
        return list(ans.values())

