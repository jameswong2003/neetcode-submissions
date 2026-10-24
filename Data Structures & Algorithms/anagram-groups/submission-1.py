class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            alphabets = [0] * 26

            for c in s:
                idx = ord(c) - ord('a')
                alphabets[idx] += 1
            d[tuple(alphabets)].append(s)
        
        return list(d.values())