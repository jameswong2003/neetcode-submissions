class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(st, l, r):
            while l < r:
                if st[l] != st[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPal(s, i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res