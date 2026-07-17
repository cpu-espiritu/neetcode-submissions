class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for idx, num in enumerate(nums):
            x = target - num
            if x in d:
                return [min(idx, d[x]), max(idx, d[x])]
            d[num] = idx        
