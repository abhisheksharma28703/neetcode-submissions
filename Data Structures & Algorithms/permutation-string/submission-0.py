class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        for i in range(len(s2)-n+1):
            temp = list(s1)

            for char in s2[i:i+n]:
                if char in temp:
                    temp.remove(char)
                else:
                    break
            if(len(temp)==0):
                return True

        return False