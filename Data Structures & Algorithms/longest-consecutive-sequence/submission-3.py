class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        out = 0

        for num in seen:
            candidate = 1
            if num-1 not in seen:
                while True:
                    if num+1 in seen:
                        candidate += 1
                        num += 1
                    else:
                        break
            out = max(out,candidate)

        return out