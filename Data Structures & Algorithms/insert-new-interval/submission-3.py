class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 3 cases:  1) new interval goes before curr 
        #           2) new interval goes after curr
        #           3) merge (update newInterval in case we merge with others)

        ans = [] 

        for i in range(len(intervals)):
            #case 1
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            #case 2 
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            #case 3
            else: 
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # if merged (case 3), and case 1 never returned
        # means continuted till end 
        ans.append(newInterval)

        return ans 
