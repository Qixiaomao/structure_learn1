class SingleNode:
    '''单链表节点'''
    def __init__(self,item) -> None:
        self.item = item
        self.next = None
        
class SingleList(SingleNode):
    '''单链表'''
    def __init__(self) -> None:
        self._head =None
        
    def is_empty(self):
        '''判断链表是否为空'''
        return self._head == None
    
    def length(self):
        '''链表长度'''
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向none，当未达到尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count
    
    def travel(self):
        '''遍历整个链表'''
        cur = self._head
        while cur != self._head:
            print(cur.item)
            cur = cur.next
        return True
        
    def add(self,item):
        '''头部添加元素'''
        node = SingleNode(item)
        node.next = self._head
        self._head = node
        
    def append(self,item):
        '''尾部添加元素'''
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            
    def insert(self,pos,item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        # 指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1,初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
            
    def remove(self,item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
                
    def search(self,item):
        '''查找节点是否存在，并返回true or false'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
           
            return False
    def printall(self):
        '''打印整个链表'''
        cur = self._head
        if cur:
            print(f"{cur.item}",end="")
            cur = cur.next
        while cur:
            print(f"->{cur.item}",end="")
            cur = cur.next 
        print("\n",flush=True)
        
if __name__ == '__main__':
    l = SingleList()
    for i in range(1,4):
        l.add(i)
    l.append(4)
    print(l.length())
    l.printall()