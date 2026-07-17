from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        
        for num in nums:
            if d[num] > 0: 
                return True
            d[num] += 1
        
        return False