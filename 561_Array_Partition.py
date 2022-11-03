from typing import List
# 정렬후에 0 2 4 ....원소들의 합이 가장 큰 min(a, b)의 합이다

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum
    
    
#파이썬스러운?방식이라는데...
#2번쨰 원소들의 합이 최대니까 정렬후에 2번째원소(::2)값만 합쳐서 리턴하는 방식
# return sum(sorted(nums)[::2])


if __name__ == "__main__":

    a = Solution()
    b= a.arrayPairSum([1,4,3,2])

    print(b)