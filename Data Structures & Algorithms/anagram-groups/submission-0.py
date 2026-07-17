class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for string in strs:
            freq = [0] * 26
            for char in string:
                x = ord(char) - ord('a')
                freq[x] += 1
            
            d[tuple(freq)].append(string)
        
        return list(d.values())

