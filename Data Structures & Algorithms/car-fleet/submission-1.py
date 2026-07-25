class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)): 
            pairs.append([position[i], speed[i]])

        #sort and reverse into position descending order
        pairs.sort(reverse=True)


        stack = [] 

        for i in range(len(pairs)): 
            #calculate and push distance to finish  (distance difference) / speed
            stack.append((target-pairs[i][0]) / pairs[i][1])

            #pop if the preceeding car is slower (combine into fleet) 
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)
