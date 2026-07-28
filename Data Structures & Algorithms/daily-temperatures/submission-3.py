class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]

        stack = [] # monotonic increasing. pairs: (index, value)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, v = stack.pop()
                ans[index] = i - index
            else:
                stack.append((i, temperatures[i]))
        
        return ans