# 单向循环列表
class Node(object):
    '''节点'''
    def __init__(self,item:int) -> None:
        self.item = item
        self.next = None
        
class SinCyclinkedlist(object):
    '''单向循环链表'''
    def __init__(self) -> None:
        self._head = None
        
    def is_empty(self):
        '''头节点为空即为空'''
        return self._head == None
    
    def length(self):
        '''返回链表的长度
        如果链表为空，返回长度为0
        '''
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next 
        return count
    
    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return 
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next 
            print(cur.item)
        print("")
        
    def add(self,item):
        '''头部添加节点'''
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            '''添加节点指向_head
             移到链表尾部，将尾部节点的next指向Node
            '''
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            self._head = node
            
    def append(self,item):
        '''尾部添加''' 
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            '''移动到链表尾部'''
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head
            
    def insert(self,pos,item):
        '''在指定位置插入'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
            
    def remove(self,item):
        '''删除一个节点'''
        if self.is_empty():
            return
        cur = self._head
        pre = None
        