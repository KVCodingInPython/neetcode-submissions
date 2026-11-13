class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if (ord(s[left]) < 48 or (ord(s[left]) > 57 and ord(s[left]) <= 64) or (ord(s[left]) >= 91 and ord(s[left]) <= 96) or ord(s[left]) > 123):
                left += 1
                continue
                
            
            if ((ord(s[right]) < 48 or (ord(s[right]) > 57 and ord(s[right]) <= 64) or (ord(s[right]) >= 91 and ord(s[right]) <= 96) or ord(s[right]) > 123)):
                right -= 1
                continue
               

            if s[left].lower() != s[right].lower():
                return False
            
            left = left + 1
            right = right - 1
            
        return True
        