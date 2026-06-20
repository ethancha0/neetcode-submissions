class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        ans = [] 
        nums.sort()

        for i in range(len(nums)):
            end = len(nums) - 1 
            j = i+1

            #skipping dupes for i 
            if i > 0 and nums[i] == nums[i-1]:
                continue


            while j < end: 
                sum = nums[i] + nums[j] + nums[end]

                if sum == 0:
                    ans.append([nums[i], nums[j], nums[end]])
                    
                    while j+1 < end and nums[j] == nums[j+1]:
                        j += 1
                    while end-1 > j and nums[end] == nums[end-1]:
                        end -=1 
                    
                    # move both ptrs inwards after found
                    j+=1
                    end -= 1
                
                elif sum < 0: 
                    j += 1
                else:
                    end -= 1
        
        return ans
        


        