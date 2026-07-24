class TimeMap:

    def __init__(self):
        self.timeStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStore:
            self.timeStore[key] = [] 
        self.timeStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeStore or not key in self.timeStore: 
            return ""

        values = self.timeStore[key]

        left = 0 
        right = len(values)-1
        ans = ""

        while left <= right:
            mid = left + (right-left) // 2
            if values[mid][1] <= timestamp:
                left = mid + 1 
                ans = values[mid][0]
            else:
                right = mid - 1 
        
        return ans


