class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = [] 

        #first elem should be sorted in ascending order
        intervals.sort() 

        for i in range(len(intervals)):
            #overlap: curr interval's start is before prev's end
            if ans and intervals[i][0] <= ans[-1][1]:
                s, e = ans.pop() 
                ans.append(
                    [min(intervals[i][0], s),
                    max(intervals[i][1], e)
                    ]
                )

            #no overlap
            else: 
                ans.append(intervals[i])

        return ans


