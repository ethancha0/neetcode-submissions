class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = [] 
        for i in range(len(intervals)): 
            #case 1: new interval is completely before curr
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #case 2: new interval is completely after curr
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # we just append curr, since we likely need to combine later
            #case 3: combine
            else: 
                newInterval = [
                                min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])
                            ]

        res.append(newInterval) # in case case #1 never runs again
        return res
                    

