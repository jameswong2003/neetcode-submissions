class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) * 2):
            idx = (i + len(nums)) % len(nums)
            ans.append(nums[idx])
        return ans