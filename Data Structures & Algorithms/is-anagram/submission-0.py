class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = []
        for c in s:
            temp.append(c)
        
        for i in t:
            if i in temp:
                temp.remove(i)
            else:
                return False
        return not temp
        
