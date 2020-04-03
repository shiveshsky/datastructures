class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, x):
        if len(self.stk)==0:
            self.stk.append(x)
            self.min_stk.append(x)
        else:
            if self.min_stk[-1]>=x:
                self.min_stk.append(x)
            self.stk.append(x)
        return x

    # @return nothing
    def pop(self):
        if len(self.stk)==0:
            pass
        else:
            pop = self.stk.pop()
            if pop == self.min_stk[-1]:
                self.min_stk.pop()

    # @return an integer
    def top(self):
        if len(self.stk)>0:
            return self.stk[-1]
        return -1

    # @return an integer
    def getMin(self):
        if len(self.min_stk) > 0:
            return self.min_stk[-1]
        return -1


