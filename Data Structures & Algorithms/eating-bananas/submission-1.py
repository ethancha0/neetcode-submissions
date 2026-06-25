class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # min hour is 1, max is the largest elem in piles 
        # we can use binary search to find the first True,

        left = 1 
        right = max(piles)
        minHours = right


        while left <= right: 
            mid = left + (right - left) // 2 

            # check if mid is a valid k eating speed value
            totalHours = 0
            for i in range(len(piles)):
                totalHours += math.ceil(piles[i] / mid)


            # move mid based on 
            if totalHours <= h: 
                minHours = mid
                right = mid - 1 
            else: 
                left = mid + 1

        return minHours

                