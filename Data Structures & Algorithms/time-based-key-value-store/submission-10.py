class TimeMap:

    def __init__(self):
        self.slovnik = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.slovnik.keys():
            self.slovnik[key] = [(timestamp,value)]
        else:
            self.slovnik[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        empty = ''
        if key not in self.slovnik.keys():
            return empty
        l = 0
        r = len(self.slovnik[key])-1

        if self.slovnik[key][-1][0]<timestamp:
            return self.slovnik[key][-1][1]
        time_prev = 0
        bolo = False
        while l<=r:
            mid = (l+r)//2
            if self.slovnik[key][mid][0]==timestamp:
                return self.slovnik[key][mid][1]
            if self.slovnik[key][mid][0]<timestamp:
                bolo = True
                time_prev = max(time_prev,mid)
                l = mid + 1
            else:
                r = mid - 1
        if bolo:
            return self.slovnik[key][time_prev][1]
        return empty