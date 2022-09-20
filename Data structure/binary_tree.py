'''
Pre-order,in-order and post-order traversal of binary trees.
Author:Seven
'''

class TreeNode:
    def __init__(self,data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class Preorder(TreeNode):
    def preorder(self,root:TreeNode):
        res = []
        
        def travesel(root:TreeNode):
            if root == None:
                return 
            res.append(root) #根节点
            self.preorder(root.left) #左节点
            self.preorder(root.right) #右节点
        travesel(root)
        return res 
    
    
    
if __name__ == '__main__':
    t = [1,3,5,6,9,10]
    p = Preorder(t)
    print(p)
    
               