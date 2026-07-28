class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # stack, check top if overlapping, if so merge
        stack = []

        #sort in ascending order
        intervals.sort() 

        for i in range(len(intervals)):
            #curr's start is before prev's end 
            if stack and intervals[i][0] <= stack[-1][1]:
                s, e = stack.pop() 
                stack.append([
                    min(intervals[i][0], s),
                    max(intervals[i][1], e)
                ])
            
            else: 
                stack.append(intervals[i])

        return stack