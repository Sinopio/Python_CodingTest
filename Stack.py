class Stack:
    def __init__(self):
        self.stack = []
         
    def push(self, data):
        self.stack.append(data)
        
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def printStack(self):
        print(self.stack)
    
if __name__ == "__main__":
    s = Stack()
    
    s.push(0)
    s.push(1)
    s.push("a")
    
    s.printStack()
    
    print(s.peek())
    print(s.pop())
    
    s.printStack()