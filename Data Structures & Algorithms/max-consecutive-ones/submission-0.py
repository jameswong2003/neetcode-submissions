class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx_count = 0
        curr_count = 0
        for n in nums:
            if n == 1:
                curr_count += 1
                continue
            mx_count = max(mx_count, curr_count)
            curr_count = 0
        
        return max(mx_count, curr_count)
