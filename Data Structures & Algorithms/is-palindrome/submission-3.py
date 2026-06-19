class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_new = ''.join(char for char in s.lower() if char.isalnum())
        
        left = 0
        right = len(s_new)-1

        while(left < right):
            
            if(s_new[left]==s_new[right]):
                left += 1
                right -= 1
            else:
                return False
        return True