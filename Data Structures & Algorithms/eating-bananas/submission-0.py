class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            current_hours = 0
            for p in piles:
                current_hours += math.ceil(float(p) / k)
            
            if current_hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res