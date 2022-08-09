# 定义线性表的顺序存储



class SqList:
    def __init__(self) -> None:
        self._data = []
    
        
    def Listlength(self) -> None:
        return len(self._data)
    
    
    def Listempty(self):
        if len(self._data) == 0:
            return True
        else:
            return False
    
    def Getelem(self,index:int) -> int:
        return self._data[index-1]
    
    def Localelem(self,e:int):
        for i in range(len(self._data)):
            if self._data[i] == e:
                return i
            else:
                return 0
    
    def Listinsert(self,index:int,e:int):
        if index < 0 | index > len(self._data):
            return False
        else:
            self._data.insert(index,e)
            return True
        
    def Listdelete(self,index:int):
        if index < 0 | index > len(self._data):
            return False
        else:
            self._data.pop(index)
            return True
        
    def Printall(self):
        print(self._data)
        
        
if __name__ == '__main__':
    s = SqList()
    
    s.Listinsert(0,1)
    s.Listinsert(1,2)
    s.Listinsert(2,3)
    s.Printall()
    s.Listlength()
    s.Listdelete(2)
    s.Printall()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
            
            
        