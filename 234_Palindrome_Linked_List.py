from typing import List
from typing import Deque
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        
        return True
    
#listnode에 하나씩 넣어줘야 답이 나오는듯
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = None
    
    aa = Solution()
    print(aa.isPalindrome(a))