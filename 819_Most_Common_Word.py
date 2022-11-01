import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [
            #리스트 컴프리핸션 활용
            #정규식으로(\w = [a-zA-Z0-9_], ^ = not) 문자나 숫자가 아닌것들을 ' '로 치활
            #후에 소문자로변환, 나누기
            #조건 = banned가 아닐것
            word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
            if word not in banned
            ]

        print(words)

        #자주 쓰는것! 기억할것
        #원소중에 같은것들의 숫자를 카운팅한다
        counts = collections.Counter(words)

        print(counts)
        # collections.Counter(a).most_common(n) : a의 요소를 세어, 최빈값 n개를 반환합니다
        # most_common(1)[0][0]을 하면 반환값이 1개라서 runtime가 줄어들긴한다
        print(counts.most_common(2))
        
        return counts.most_common(1)[0][0]
    
    
if __name__ == "__main__":


    a = Solution()
    b = a.mostCommonWord("apple banana kang kang kang banana", ["apple", "kim"])
    print(b)