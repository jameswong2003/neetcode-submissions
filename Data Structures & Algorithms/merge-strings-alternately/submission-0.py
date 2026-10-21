class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pointer, word2_pointer = 0, 0

        res = []
        while word1_pointer < len(word1) and word2_pointer < len(word2):
            res.append(word1[word1_pointer])
            res.append(word2[word2_pointer])
            word1_pointer += 1
            word2_pointer += 1
        
        if word1_pointer < len(word1):
            res.extend(word1[word1_pointer:])
        if word2_pointer < len(word2):
            res.extend(word2[word2_pointer:])
        return "".join(res)