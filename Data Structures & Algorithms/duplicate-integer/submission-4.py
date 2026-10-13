class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        newlist = set()
        for i in nums:
            if i in newlist:
                return True
            newlist.add(i)
        return False