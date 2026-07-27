class Solution:
    def isPalindrome(self,s):
            return s[::-1] == s
            
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxLen = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.isPalindrome(s[i:j+1]):
                    if len(s[i:j+1])>maxLen:
                        maxLen = len(s[i:j+1])
                        res = s[i:j+1]
        return res
        