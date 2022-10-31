class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1
        
    def InsertFirst(self, data):
        new_node = Node(data)
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.list_size += 1

    def SelectNode(self, num):
        if self.list_size < num:
            return
        
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
            
        #node 값이 필요하면 node.data
        return node
    
    def InsertMiddle(self, num, data):
        if self.head.next == None:
            InsertLast(data)
            return
        
        node = self.SelectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1
        
    def InsertLast(self, data):
        node = self.head

        while True:
            if node.next == None:
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1
          
        
    def __str__(self):
        print_list = '['
        node = self.head
        while True:
            print_list += str(node.data)
            if node.next == None:
                break
            node = node.next
            print_list += ", "
        print_list += "]"
        return print_list
    
    def DeleteHead(self):
        node = self.head
        self.head = node.next
        self.list_size -= 1
        del node
        
    def DeleteNode(self, num):
        if self.list_size < 1:
            return 
        elif self.list_size < num:
            return
        
        if num == 0:
            self.DeleteHead()
            
        node = self.SelectNode(num-1)
        node.next = node.next.next
        del_node = node.next
        self.list_size -= 1
        del del_node
        
    def Size(self):
        return str(self.list_size)
    
if __name__ == "__main__":
    
    a = SingleLinkedList(100)
    print(a)

    a.InsertLast(200)
    a.InsertLast(300)
    print(a)


    #헤더 교체
    a.InsertFirst(1000)
    a.InsertFirst(3000)
    print(a)

    #중간에 삽입
    a.InsertMiddle(1, 999)
    print(a)
    a.InsertMiddle(5, 999)
    print(a)


    #중간 인덱스
    a.DeleteNode(2)
    print("after mid delete:\n{}".format(a))

    #헤더 삭제
    a.DeleteHead()
    print("after head delete:\n{}".format(a))

    #리스트 크기 확인
    print(a.Size())

            