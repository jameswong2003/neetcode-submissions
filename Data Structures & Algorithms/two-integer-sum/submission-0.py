class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = dict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in history:
                return [history[diff], i]
            history[nums[i]] = i
        