class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = [] 

        for i in range(len(temperatures)): 
            #compare to top of stack
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                top = stack.pop()[1]
                ans[top] = i - top 

            else: 
                stack.append((temperatures[i], i))

        return ans