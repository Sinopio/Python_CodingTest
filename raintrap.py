from typing import List

class Solution:
    def trapTwoPointer(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume
    
if __name__ == "__main__":
    
    a = Solution()
    b = a.trapTwoPointer([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    
    print(b)