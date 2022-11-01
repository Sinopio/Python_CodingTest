from typing import List

class Solution:
    def reverseStrig(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)
        
        
if __name__ == "__main__":
    s = "HelloWorld"
    print(s[::-1])