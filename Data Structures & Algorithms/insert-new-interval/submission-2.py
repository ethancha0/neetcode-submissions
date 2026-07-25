class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = [] 

        for i in range(len(intervals)): 
            #case 1: new is completely before current 
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]

            #case 2: new is completely after current 
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])

            #case 3: merge needed
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                            max(newInterval[1], intervals[i][1])]


        ans.append(newInterval)

        return ans