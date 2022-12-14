class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
    

if __name__=="__main__":

    #-----------------------
    #list 1 생성
    head = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)


    head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None
    #여기까지 리스트 연결

    #출력 확인
    q = []
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    print(q)

    #---------------------
    #뒤집기
    aa = Solution()
    aa.reverseList(head)

    #뒤집은 후 출력 확인
    q = []
    node = e  #위치가 뒤 바뀜
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)