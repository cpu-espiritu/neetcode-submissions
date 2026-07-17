class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for letter in s:
            s_dict[letter] += 1
        
        for letter in t:
            t_dict[letter] += 1

        for letter in s_dict.keys():
            print(letter)
            if s_dict[letter] != t_dict[letter]:
                return False
        
        return True