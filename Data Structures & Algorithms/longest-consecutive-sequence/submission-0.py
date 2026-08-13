class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        out = 0

        for num in nums:
            seen.add(num)

        for num in seen:
            if num-1 not in seen:
                candidate = [num]
                while True:
                    if num+1 in seen:
                        candidate.append(num+1)
                        num += 1
                    else:
                        break
            out = max(out,len(candidate))

        return out