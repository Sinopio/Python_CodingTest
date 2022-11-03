import collections
import hashlib

class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
    
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스위치에 노드가 없다면 노드 삽입 후 종료
        # self.table[index] is None이 아니라 value값을 확인한이유
        # >> defaultdict은 없는 값을 찾으면 해당자리에 default값을 가진
        #    새로운 인자를 만들어 버리기때문
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 만약 겹친다면 연결리스트로 다음 자리에?위치
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            # 다음이 None라면 여기서 멈추고 while문 탈출 
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        index = key % self.size
        
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
    def remove(self, key: int) -> None:
        index = key % self.size
        
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        prev = p
        while p:
            if p.key ==  key:
                prev.next = p.next
                return
            prev, p = p, p.next
            
            

if __name__=="__main__":
    
    a = MyHashMap()
    a.put(10,1)
    a.put(20,25)
    a.put(45,15)

    print(a.get(10))
    print(a.get(20))
    a.remove(10)
    print(a.get(10))