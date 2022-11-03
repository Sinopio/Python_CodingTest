class MyCircularQueue:
    def __init__(self, len: int):
        self.queue = [None] * len
        self.maxlen = len
        self.front = 0
        self.rear = 0
        
    def enQueue(self, value: int) -> bool:
        # rear가 none이라면(비어있다면)
        if self.queue[self.rear] is None:
            # rear위치에 value저장
            self.queue[self.rear] = value
            # rear포인터를 1칸뒤로 이동
            self.rear = (self.rear + 1) % self.maxlen
            return True
        
        # rear위치에 값이 있다면
        else:
            return False
        
    def deQueue(self) -> bool:
        # front위치에 값이 비어있으면 뺼게 없다!
        if self.queue[self.front] is None:
            return False
        
        # front위치에 값이 없다면 비었으니까 값을 빼고
        # front 포인터를 한칸뒤로 이동
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True
    
    def Front(self) -> int:
        val = 0
        
        if self.queue[self.front] == None:
            val = None 
        else:
            val = self.queue[self.front]
            
        return val
        
    #    return -1 if self.queue[self.front] is None else self.queue[self.front]
    
    def Rear(self) -> int:
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]
        
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None
    
    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None
    
    
if __name__=="__main__":

    a = MyCircularQueue(5)
    a.enQueue(10)
    a.enQueue(20)
    print(a.Front())
    b = a.deQueue()
    print(b)