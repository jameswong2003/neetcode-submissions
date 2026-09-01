class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            "1": [],
            "2": ["A", "B", "C"],
            "3": ["D", "E", "F"],
            "4": ["G", "H", "I"],
            "5": ["J", "K", "L"],
            "6": ["M", "N", "O"],
            "7": ["P", "Q", "R", "S"],
            "8": ["T", "U", "V"],
            "9": ["W", "X", "Y", "Z"]
        }
        
        res = []
        if len(digits) == 0:
            return []

        def backtrack(i, path):
            if i >= len(digits):
                res.append("".join(path))
                return
            
            for c in digits_map[digits[i]]:
                path.append(c.lower())
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res
