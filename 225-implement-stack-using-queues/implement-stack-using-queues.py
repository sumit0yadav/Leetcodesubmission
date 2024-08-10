from collections import deque
class MyStack:

    def __init__(self):
        self.q=deque()
        

    def push(self, x: int) -> None:
        q=self.q
        q.append(x)
        

    def pop(self) -> int:
        q=self.q
        x=q.pop()
        return x
        

    def top(self) -> int:
        q=self.q
        x=q.pop()
        q.append(x)
        return x
        

    def empty(self) -> bool:
        q=self.q
        return len(q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()