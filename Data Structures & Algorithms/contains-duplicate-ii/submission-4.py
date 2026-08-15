class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(k + 1):
            if i < len(nums):
                if nums[i] in s:
                    return True
                s.add(nums[i])

        l, r = 0, k + 1
        while r < len(nums):
            s.remove(nums[l])
            if nums[r] in s:
                return True
            
            s.add(nums[r])
            l += 1
            r += 1
        return False