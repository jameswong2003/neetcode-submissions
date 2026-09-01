class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, subset):
            res.append(subset.copy())

            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    continue
                
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
                
        backtrack(0, [])
        return res