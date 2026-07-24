class TimeMap:

    def __init__(self):
        self.timeMap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap: 
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:

        if not self.timeMap or not key in self.timeMap: 
            return ""

        ans = ""
        vals = self.timeMap[key]

        left = 0 
        right = len(vals)-1

        while left <= right: 
            mid = left + (right-left) // 2

            if vals[mid][1] <= timestamp:
                left = mid + 1 
                ans = vals[mid][0]
            else:
                right = mid - 1 

        return ans
