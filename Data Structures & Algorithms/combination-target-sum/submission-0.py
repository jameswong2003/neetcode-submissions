class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(idx, path, total):
            if idx >= len(nums) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return

            path.append(nums[idx])
            backtrack(idx, path, total + nums[idx])
            path.pop()
            backtrack(idx + 1, path, total)
        
        backtrack(0, [], 0)
        return res