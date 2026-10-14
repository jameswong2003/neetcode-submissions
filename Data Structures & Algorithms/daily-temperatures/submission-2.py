class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        result = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = idx - stack_index
            stack.append((temp, idx))
        return result