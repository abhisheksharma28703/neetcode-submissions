class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
           return False
        temp1 = [0]*26
        temp2 = [0]*26
        matches = 0
        for i in range(len(s1)):
            temp1[ord(s1[i])-ord('a')]+=1
            temp2[ord(s2[i])-ord('a')]+=1
        matches = 0
        for i in range(26):
            if temp1[i] == temp2[i]:
                matches += 1
            else :
                matches = matches
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r])-ord('a')
            temp2[index] += 1
            if temp2[index] == temp1[index]:
                matches += 1
            elif temp2[index] == temp1[index]+1:
                matches -= 1
            index = ord(s2[l])-ord('a')
            temp2[index] -= 1
            if temp2[index] == temp1[index]:
                matches += 1
            elif temp2[index] == temp1[index]-1:
                matches -= 1
            l += 1
        return matches == 26
            
        
