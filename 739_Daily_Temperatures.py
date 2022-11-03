from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        
        for index, cur_value in enumerate(T):
            
            while stack and cur_value > T[stack[-1]]:
                
                last = stack.pop()
                
                answer[last] = index - last
                
            stack.append(index)

        return answer
    
if __name__=="__main__":

    #-----------------------
    s= [73, 74, 75, 71, 69, 72, 76, 73]
    a = Solution()
    result = a.dailyTemperatures(s)
    print("result:{}".format(result))