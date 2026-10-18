class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s)-1

        while front < back:
            if not s[front].lower().isalnum():
                front += 1
            elif not s[back].lower().isalnum():
                back -= 1
            elif s[front].lower() != s[back].lower():
                return False
            else:
                front += 1
                back -= 1
        
        return True