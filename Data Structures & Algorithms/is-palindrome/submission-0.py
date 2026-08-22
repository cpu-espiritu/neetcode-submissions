class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        front, back = 0, len(s) - 1
        
        while front < back:
            if s[front].isalnum():
                if s[back].isalnum():
                    if s[front] != s[back]:
                        return False
                    front += 1
                    back -= 1
                else:
                    back -= 1
            else:
                front += 1
        
        return True