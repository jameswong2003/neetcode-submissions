class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]

        count_dict = dict()
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1
        
        for key, value in count_dict.items():
            count[value].append(key)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res