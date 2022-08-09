# 实现顺序栈
class Sqlstack:
    def __init__(self):
        self.MaxStackSize = 10
        self.s = [None for i in range(self.MaxStackSize)]
        self.top = -1
        
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def push(self,data:int):
        if self.top != self.MaxStackSize - 1:
            self.top += 1
            self.s[self.top] = data
        else:
            return False
        
    def LengthStack(self):
        return self.top + 1
        
    def pop(self):
        if self.isempty():
            print('栈空')
            return -1
        else:
            e = self.s[self.top]
            self.top -= 1
            return e
        
    def printfall(self):
        print(self.s)
        
        
if __name__ == '__main__':
    s = Sqlstack()
    
   
    
    for i in range(0,5):
        s.push(i)
    s.printfall()
    s.pop()
    s.printfall()
        

        