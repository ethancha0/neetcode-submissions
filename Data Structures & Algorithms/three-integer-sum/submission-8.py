class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        #pointers: front, front+1, end
        #-4, -1, -1, 0, 1, 2
        ans = []

        for i in range(len(nums)):
            #skip dupes for first elem 
            if i > 0 and nums[i] == nums[i-1]:
                continue

            front = i + 1
            end = len(nums)-1

            while front < end: 
                total = nums[i] + nums[front] + nums[end]
                if total < 0: 
                    front += 1 
                elif total > 0: 
                    end -= 1 
                else: 
                    ans.append([nums[front], nums[i], nums[end]])
                    
                    #skip duplicates
                    while front < end and nums[front] == nums[front+1]:
                        front += 1 
                    while front < end and nums[end] == nums[end-1]:
                        end -=1

                    front += 1
                    end -= 1 

        
        return ans





