import collections


class MyStack:
    def __init__(self):
        #데크로 구현해서 앞에서 뺄수있게
        self.q = collections.deque()

    def push(self, x):
        
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            # 뒤에 넣은 후에 앞에서부터 차례대로 빼서 다시 뒤어 넣는다
            # ㅁㄴㅇ <<ㄹ > ㄴㅇㄹ <<ㅁ > ㅇㄹㅁ << ㄴ > ㄹㅁㄴ << ㅇ
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

if __name__=="__main__":

    a = MyStack()
    a.push(10)
    a.push(20)
    b = a.pop()
    print(b)