class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # combine arrs
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        # reverse and sort in descending positions (closest to finish)
        cars.sort(reverse=True)

        stack = [] # keep times till finish

        for p, s in cars:
            # time to finish = (distance difference) / speed
            timeFinish = (target-p) / s
            
            if stack and stack[-1] >= timeFinish:
                continue
            else: 
                stack.append(timeFinish)

        
        return len(stack)

            

