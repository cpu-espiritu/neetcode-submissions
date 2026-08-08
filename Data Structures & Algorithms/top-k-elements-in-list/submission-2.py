class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        freqDist = [[] for i in range(len(nums)+1)]
        
        for (num, freq) in counts.items():
            freqDist[freq].append(num)

        out = []
        for i in range(len(nums), 0, -1):
            for num in freqDist[i]:
                if k <= 0:
                    return out
                else:
                    out.append(num)
                    k -= 1
        return out

