class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0 for _ in range(len(temperatures))]

        # stack: (temperature, index) 
        stack = [] 
        for i, t in enumerate(temperatures): 
            while stack and t > stack[-1][0]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop() 

            stack.append((t, i))

        return ans 
