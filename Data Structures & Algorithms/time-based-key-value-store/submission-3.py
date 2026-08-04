class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.cache:
            return ""
            
        values = self.cache[key]
        L, R = 0, len(values) - 1

        while L <= R:
            m = (L+R)//2
            
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] > timestamp:
                R = m - 1
            else:
                L = m + 1

        return values[R][1] if values[R][0] < timestamp else ""


