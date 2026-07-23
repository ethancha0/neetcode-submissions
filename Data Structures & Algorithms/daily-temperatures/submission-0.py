class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            #check if greater than stack top 
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                index = stack.pop()[1]
                ans[index] =  i - index
            else: 
                stack.append((temperatures[i], i))
        
        return ans