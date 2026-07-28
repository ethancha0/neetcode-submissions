class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        left = 1
        right = max(piles)
        ans = -1

        while left <= right:
            mid = left + (right-left) // 2 

            hours = 0 
            for p in piles: 
                hours += math.ceil(p / mid)

            if hours <= h:
                right = mid -1
                ans = mid
            else: 
                left = mid + 1 
        
        return ans
