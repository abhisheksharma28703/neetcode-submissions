class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    temp[i] = j-i
                    break
        return temp


