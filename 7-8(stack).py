from turtle import distance
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int :
        #height = [0,1,0,2,1,0,1,3,2,1,2,1]
        stack = []
        volume = 0
    
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
            
                top = stack.pop()
            
                if not len(stack):
                    break
            
                distance = i - stack[-1] -1
            
                waters = min(height[i], height[stack[-1]]) - height[top]
        
                volume += distance * waters
        
            stack.append(i)
    
        #print(volume)
    
        return volume
    
if __name__ == "__main__":
    
    a = Solution()
    result = a.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    
    print(result)
    