class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # first sort in ascending order
        intervals.sort()

        ans = [] 

        for i in range(len(intervals)):
            #case1: newInterval goes completely before current
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]

            #case2: newInterval goes completely after current
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])

            #case3: merge. update newinterval
            else: 
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]


        #append + return if case1 never returned
        ans.append(newInterval)
        return ans
