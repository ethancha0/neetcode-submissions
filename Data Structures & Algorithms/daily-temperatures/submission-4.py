class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack: val : index
        # when we encounter a warmer day, we pop, and add difference in indicies to ans 

        ans = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                poppedVal, poppedIndex = stack.pop() 
                ans[poppedIndex] = i - poppedIndex
            else:
                stack.append((temperatures[i], i))

        return ans