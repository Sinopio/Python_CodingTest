#근데 왜 2중 for문이 더 빠르지?

import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagrams를 딕셔너리화? 시킨다
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            #join을통해 원소사이사이에 ''를 넣어준다
            #단어를 정렬한 후 같은 단어라면 value값에 넣어준다
            anagrams[''.join(sorted(word))].append(word)
            
            print(anagrams)
            print("-------------")

        return list(anagrams.values())
    
if __name__ == "__main__":
    a = Solution()
    b = a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(b)
    