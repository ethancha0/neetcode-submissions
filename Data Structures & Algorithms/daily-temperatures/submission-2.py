class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (value, index)
        ans = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                popped = stack.pop()
                ans[popped[1]] = i - popped[1]
            else: 
                stack.append((temperatures[i], i))

        return ans