class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        minSpeed = right

        while left <= right: 
            mid = left + (right-left) // 2 

            #check is mid a valid eating speed 
            k = 0 
            for elem in piles: 
                k += math.ceil(elem / mid)

            if k <= h: 
                minSpeed = min(minSpeed, mid)
                right = mid - 1 
            else: 
                left = mid + 1 

        return minSpeed
