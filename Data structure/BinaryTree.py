


class Node(object):
    '''树的节点'''
    def __init__(self,elem=-1,lchild=None,rchild=None) -> None:
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
        
class Tree(object):
    '''树类'''
    def __init__(self,root=None) -> None:
        self.root = root
        
    def add(self,elem):
        '''为树添加节点'''
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return 
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
                    
    # 深度遍历：包括先序遍历，中序遍历，后序遍历
    def preorder(self,root):
        '''先序遍历:先访问根，再访问左子树，再访问右子树'''
        if root == None:
            return 
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)
        
    def inorder(self,root):
        '''中序遍历：先访问左子树，在访问根节点，最后访问右子树'''
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)
        
    def postorder(self,root):
        '''后序遍历：先访问左子树，再到右子树，最后根节点'''
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)
        
    def breadth_travel(self,root):
        '''广度优先遍历（层次遍历）：利用队列实现'''
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)
        
        
    
    
                    
if __name__ == '__main__':
    t = Tree()
    for i in range(1,5):
        t.add(i)
    