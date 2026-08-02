class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if t == '' : return
        countT = Counter(t)
        window = {}
        l = 0
        have = 0
        need = len(countT)
        maxi = [-1,-1]
        maxLen = float('infinity')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1)<maxLen:
                    maxLen = r-l+1
                    maxi = [l,r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = maxi
        return s[l:r+1] if maxLen != float('infinity') else ''
                




            