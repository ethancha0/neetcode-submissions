class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)


        while left < right: 
            mid = left + (right-left) // 2

            # check if the mid is a valid eating rate 
            hours = 0 
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h: 
                right = mid

            elif hours > h:
                left = mid + 1 
        
        return left