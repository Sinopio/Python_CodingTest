from dataclasses import dataclass
from multiprocessing import set_forkserver_preload
from traceback import print_list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = None
        self.list_size = 1
        
    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            if node:
                print_list += str(node.data)
            if node == self.tail:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        
        return print_list
    
    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node
        self.list_size += 1
        
    def insertMiddle(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1
        
    def insertLast(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.list_size += 1
        
    def selectNode(self, num):
        if self.list_size < num:
            print("Overflow!!")
            return
        
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return
        elif self.list_size < num:
            return
        
        if num == 0:
            self.deleteHead()
            return
        
        node = self.selectNode(num -1)
        node.next = node.next.next
        del_node = node.next
        del del_node
        
    def deleteHead(self):
        node =self.head
        self.head = node.next
        del node
    
    def size(self):
        return str(self.list_size)
    
    def get_head_tail(self):
        return self.head.data, self.tail.data
    
if __name__ == "__main__":

    a = CircleLinkedList(100)
    print(a.size())


    a.insertFirst(999)
    a.insertFirst(9990)


    a.insertLast(77)

    a.insertMiddle(2, 500)

    b, c = a.get_head_tail()

    print("head:{} tail:{}".format(b, c))


    print(a)