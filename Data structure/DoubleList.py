class Node(object):
    '''双向链表节点'''
    def __init__(self,item) -> None:
        self.item = item
        self.prev = None
        self.next = None
        
class Dlinklist(object):
    '''双向链表'''
    def __init__(self) -> None:
        self._head = None
        
    def is_empty(self):
        '''判断是否为空'''
        return self._head == None
    
    def length(self):
        '''返回链表的长度'''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        '''遍历链表'''
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next 
        print("")
        
    def add(self,item):
        '''头部插入'''
        node = Node(item)
        if self.is_empty():
                #若为空，将_head指向Node
                self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # _head的头节点的prev指向Node
            self._head.prev = node
            # _head指向node
            self._head = node
            
    def append(self,item):
        '''尾部插入元素'''
        node = Node(item)
        if self.is_empty():
            # 空链表，_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur 的next 指向Node
            cur.next = node
            # 将node的Prev指向cur
            node.prev = cur
        
    def search(self,item):
        '''查找元素是否存在'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
    def insert(self,pos,item):
        '''在指定位置添加节点'''
        if pos <= 0:
            self.add(item)
        if pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将Node的prev指向cur
            node.prev = cur
            # 将Node=next指向cur的下一个节点
            cur.next.prev = node
            # 将cur的下一个节点的prev指向Node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node
            
    def remove(self,item):
        '''删除元素'''
        if self.is_empty():
            return 
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的Prev设置为none
                    cur.next.prev = None
                    # _head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点next指向cur的最后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next
                
if __name__ == "__main__":
    ll = Dlinklist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print(f"length:{ll.length()}")
    ll.travel()
    print(ll.search(3))
    
    ll.remove(1)
    print(f"length:{ll.length()}")
    ll.travel() 
    