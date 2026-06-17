class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # temp = []
        # for c in s:
        #     temp.append(c)
        
        # for i in t:
        #     if i in temp:
        #         temp.remove(i)
        #     else:
        #         return False
        # return not temp

        if(len(s)!=len(t)):
            return False
        
        temp = [0]*26

        for i in s:
            temp[ord(i)-ord('a')]+=1
        
        for i in t:
            idx = ord(i)-ord('a')
            temp[idx] -= 1
            if temp[idx]<0:
                return False
        return True

