class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort in asc order
        intervals.sort()

        # [1,2], [1, 4], [2, 4]
        prevEnd = intervals[0][1]
        count = 0 

        for i in range(1, len(intervals)): 
            if intervals[i][0] < prevEnd: 
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else: 
                prevEnd = intervals[i][1]


        return count
