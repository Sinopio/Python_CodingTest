
class Queue:
    def __init__(self):
        self.queue = []
    
    def dequeue(self):
        # 길이가 0일때 디큐하려고하면 오류처리
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    
    def enqueue(self, n):
        self.queue.append(n)
        pass
    
    def printQueue(self):
        print(self.queue)
        
if __name__ == "__main__":
    a = Queue()
    
    a.enqueue("a")
    a.enqueue(3)
    a.enqueue("b")
    
    a.printQueue()
    
    a.dequeue()
    print(a.dequeue())
    
    a.printQueue()