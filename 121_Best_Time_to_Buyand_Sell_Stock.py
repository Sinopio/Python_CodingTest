from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #별 의미는 없고 시스템상 최댓값을 min_price에 저장해서
        #비교되도록 한것이다.
        min_price = sys.maxsize
        print(min_price)
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
    
if __name__ == "__main__":

    #===========================
    a = Solution()
    b= a.maxProfit([1,4,3,6,2])

    print(b)
    #===========================