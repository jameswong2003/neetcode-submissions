class TimeMap:

    def __init__(self):
        self.keyStore = {} # key, list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.keyStore.get(key, [])
        l, r = 0, len(key_list) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2
            if key_list[m][1] <= timestamp:
                res = key_list[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
