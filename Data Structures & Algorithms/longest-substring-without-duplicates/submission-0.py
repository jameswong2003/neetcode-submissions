class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        history = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in history:
                history.remove(s[l])
                l += 1
            
            history.add(s[r])
            res = max(res, len(history))
        return res