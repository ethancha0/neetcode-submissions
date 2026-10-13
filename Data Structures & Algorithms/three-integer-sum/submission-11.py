class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort: [-4, -1, -1, 0 , 1, 2 ]
        nums.sort() 

        ans = [] 
        
        for i in range(len(nums)):
            #check for dupes in front 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            front = i+1
            end = len(nums) - 1 

            while front < end: 
                winSize =  nums[i] + nums[front] + nums[end]
                if winSize < 0: 
                    front += 1 
                elif winSize > 0: 
                    end -= 1 
                else: 
                    #FOUND 
                    ans.append([nums[i], nums[front], nums[end]])

                    #fast forward if dupes 
                    while front < end and nums[front] == nums[front+1]:
                        front += 1 
                    while front < end and nums[end] == nums[end-1]:
                        end -= 1 

                    #move
                    front += 1 
                    end -= 1 

    

        return ans