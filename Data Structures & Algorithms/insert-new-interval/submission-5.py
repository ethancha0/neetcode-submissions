class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #case 1: new inserts completely before curr
        #case 2: new interval is completely after curr
        #case 3: new goes after (just change the param incase future requires merge)

        ans = []

        for i in range(len(intervals)): 
            #case 1
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans

            #case 2
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])

            #case 3
            else:
                tempStart = min(newInterval[0], intervals[i][0])
                tempEnd = max(newInterval[1], intervals[i][1])

                newInterval = [tempStart, tempEnd]


        #append new to end if case 1 never returned
        ans.append(newInterval)
        return ans
                
