class MinStack:

    def __init__(self):
        self.st=[]
        self.min=[]
        self.minval=int(1e9)

        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min or self.minval>=val:
            self.min.append(val)
            self.minval=val

        

    def pop(self) -> None:
        x=self.st.pop()
        if x==self.min[-1]:
            y=self.min.pop()
            if self.min:
                self.minval=self.min[-1]
            else:
                self.minval=int(1e9)
        



    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()