import math

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * suffix[i+1])

        return res



