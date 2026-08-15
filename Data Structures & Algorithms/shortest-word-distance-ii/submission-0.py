class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word1locs, word2locs = self.locations[word1], self.locations[word2]

        l1, l2 = 0, 0
        min_diff = float("inf")

        while l1 < len(word1locs) and l2 < len(word2locs):
            difference = abs(word1locs[l1] - word2locs[l2])
            min_diff = min(min_diff, difference)

            if word1locs[l1] < word2locs[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
