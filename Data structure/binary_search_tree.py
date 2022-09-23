'''
二叉查找树
author:最爱百香果
'''
from logging import root
import re
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
                
    def deletetree(self,data:int):
        # 删除有三种情况，分别是直接删除子节点，删除对象有一个子节点，删除对象有两个子节点
        p = TreeNode(root) #子节点，初始指向root节点
        pp = TreeNode() #父节点
        # 第一种情况
        if(p != None and p.data != data):
                    pp = p
                    if p.data > data:p.right
                    else:p.left
        if p==None:
            return
        # 第二种情况:删除一个子节点
        
        # p的子节点
        
        child = TreeNode()
        
        if (p.left != None):
            child = p.left
        elif (p.right != None):
            child = p.right
        else:
            child = None
            
        if(pp == None):root = child
        elif(pp.left == p):
            pp.left = child
        elif(pp.right == p):
            pp.right = child
            
        #第三种情况
        minp = TreeNode(None)
        minpp = TreeNode(None)
        if(p.left != None and p.right != None):
            minp = p.right
            minpp = p
            while(minp.left != None):
                minpp = minp
                minp = minp.left
            p.data = minp.data
            p = minp
            pp = minpp
        
        
                        
                    
if __name__ == '__main__':
    b = BinarySearchTree()
    b.FindTree(2)