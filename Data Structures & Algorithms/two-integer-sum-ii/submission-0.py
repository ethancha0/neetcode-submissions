class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        front = 0 
        end = len(numbers) - 1

        while front < end:
            theSum = numbers[front] + numbers[end]
            
            if theSum < target: 
                front += 1
            
            elif theSum > target: 
                end -= 1
            
            else:
              return([front+1, end+1])
        