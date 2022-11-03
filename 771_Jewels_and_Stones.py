import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # collections.Counter로 요소와 개수파악
        stone = collections.Counter(S)
        count = 0
        
        # J의 요소중에 stone에 포함되는게 있다면 개수를 더한다
        for char in J:
            count += stone[char]
        
        return count
        