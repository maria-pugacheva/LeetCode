class TimeMap:
    """A class representing a time-based key-value data structure that
    stores multiple values for the same key at different timestamps and
    retrieves the value for a key at a specific timestamp.
    """
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        i, j = 0, len(values) - 1
        while i <= j:
            m = (i + j) // 2
            if values[m][-1] == timestamp:
                res = values[m][0]
                break
            elif values[m][-1] < timestamp:
                res = values[m][0]
                i = m + 1
            else:
                j = m - 1
        return res


store = TimeMap()
store.set('car', 'honda', 1)
store.set('car', 'tesla', 2)
print(store.get('car', 1) == 'honda')
print(store.get('car', 3) == 'tesla')
