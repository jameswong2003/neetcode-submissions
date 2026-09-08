class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        pointer = 0
        n = len(nums)
        while pointer < n * 2:
            idx = pointer % n
            res.append(nums[idx])
            pointer += 1
        return res