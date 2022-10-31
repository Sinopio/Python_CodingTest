class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.data)
    
class DoubleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1
        
    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == self.head:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list
    
    def insertFirst(self, data):
        new_node = Node(data)
        if not self.head.prev == None:
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
        if not self.head.next == None:
            new_node.next = self.head.next
        self.head.prev = new_node
        self.head = new_node
        self.list_size += 1
        
    def insertMiddleAfter(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next
        node.next.preb = new_node
        node.next = new_node
        self.list_size += 1
        
    def insertMiddleBefore(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.list_size += 1
        
    def insertLast(self, data):
        new_node = Node(data)
        if self.head.next == None:
            self.head.next = new_node
            new_node.prev = self.head
        
        if not self.head.prev == None:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
        self.head.prev = new_node
        new_node.next = self.head
        self.list_size += 1
        
    def selectNode(self, num):
        if self.list_size < 1:
            return
        elif self.list_size <= num:
            return
        
        count = 0
        node = self.head
        
        while count < num:
                node = node.next
                count += 1
                
        return node
    
    def deletNode(self, num):
        if self.list_size < 1:
            return
        elif self.list_size <= num:
            return
        
        if num==0:
            self.deleteHead()
            return
        node = self.selectNode(num)
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        
    def deleteHead(self):
        node = self.head
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node.next
        del node
        
    def size(self):
        return str(self.list_size)
    
    def seeNodeData(self, num):
        if self.list_size < 1:
            return
        elif self.list_size <= num:
            return
        
        count = 0
        node = self.head
        
        while count < num:
                node = node.next
                count += 1
                
        return node.data
    
    
if __name__ == "__main__":


    a = DoubleLinkedList(100)
    print(a.size())

    a.insertLast(123)
    a.insertLast(777)
    print(a)
    a.insertMiddleAfter(1, 300)
    print(a)        
    a.insertMiddleAfter(2, 400)
    print(a)
    
    print(a.size())
    print(a)

    print(a.seeNodeData(2))
    