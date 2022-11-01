import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
    
if __name__ == "__main__":
    a = Solution()
    result = a.isPalindrome("a02120A")
    print(result)