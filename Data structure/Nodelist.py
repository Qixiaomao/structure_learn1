# 定义一个单链表



class Node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self._next = next
        

class SingleLink:
    def __init__(self) -> None:
        self.__head = None
     
        # 创建一个节点 
    def create_node(self,val):
        return Node(val)
    
    def getelem(self,index:int):
        p = self.__head
        pos = 0
        while p is not None and pos != index:
            p = p.next
            pos += 1
        return p
    
    def insert_elem_head(self,new_node:Node):
        if new_node:
            new_node._next = self.__head
            self.__head = new_node
            
    def insert_elem_index(self,index:int):
        new_node = Node(index)
        self.insert_elem_head(new_node)
    
    def insert_elem(self,node:Node,value:int):
        new_node = node(value)
        self.insert_elem_head(node,new_node)
        
    def insert_elem_trail(self,value:int):
        new_node = Node(value)
        node = Node(value)
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node
        
    def delete_elem(self,index:int):
        pass
        
    
    def print_all(self):
        cur = self.__head
        if cur:
            print(f"{cur.data}",end=" ")
            cur = cur._next
        while cur:
            print(f"->{cur.data}",end=" ")
            cur = cur._next
        print("\n",flush=True) 
        
        
if __name__ == '__main__':
    l = SingleLink()
    for i in range(10):
        l.insert_elem_trail(i)
    l.print_all()
    
    
        
                   