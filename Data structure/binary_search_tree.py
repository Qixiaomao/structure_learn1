'''
二叉查找树
author:考研落难生
'''
from logging import root
from tkinter.tix import Tree
from turtle import left


class TreeNode(object):
    def __init__(self,data:None) -> None:
        self.right = None
        self.left = None
        self.data = data
    
class BinarySearchTree(object):
    def __init__(self) -> None:
       self.node = TreeNode()
       
    def FindTree(self,val:int):
        p = self.node
        while (p != None):
            if p.data > val:
                p.right
            elif p.data < val:
                p.left
            else:
                return p
        return 
    
    def InsertNode(self,val:int):
        p = self.node
        if p == None:
            p = TreeNode(val)
            return
        while p != None:
            if p.data > val:
                if p.right == None:
                    p = TreeNode(val)
                    return 
                p = p.right
            else:
                if p.left == None:
                    p = TreeNode(val)
                    return 
                p = p.left
                
                    
            
    
if __name__ == '__main__':
    b = BinarySearchTree()
    b.FindTree(2)