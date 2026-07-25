class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # merge position and speed arrays
        pairs = []
        for i in range(len(position)): 
            pairs.append([position[i], speed[i]])

        # sort in decending order (closest position to final) 
        pairs.sort(reverse=True)
        stack = [] 

        for i in range(len(pairs)): 
            #calculate time to finish (distance difference) / speed
            stack.append((target-pairs[i][0]) / pairs[i][1]) 

            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop() 

        return len(stack)
