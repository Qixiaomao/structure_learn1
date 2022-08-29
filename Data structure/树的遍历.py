'''树的遍历分为深度遍历和广度遍历
深度优先遍历
前序遍历（递归法，迭代法）
中序遍历（递归法，迭代法）
后序遍历（递归法，迭代法）
广度优先遍历
层次遍历（迭代法）

递归遍历
确定递归函数的参数和返回值： 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 
并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。

确定终止条件： 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，
就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，
如果递归没有终止，操作系统的内存栈必然就会溢出。

确定单层递归的逻辑： 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。

'''
class TreeNode:
    def __init__(self,val=0) -> None:
        self.val = val
        self.left = None
        self.right = None

# 前序遍历-递归-LC144_二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode):
        # 保存结果
        result = []
        
        def traversal(root: TreeNode):
            if root == None:
                return
            result.append(root.val) # 前序
            traversal(root.left)    # 左
            traversal(root.right)   # 右

        traversal(root)
        return result

# 中序遍历-递归-LC94_二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)    # 左
            result.append(root.val) # 中序
            traversal(root.right)   # 右

        traversal(root)
        return result

# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode):
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)    # 左
            traversal(root.right)   # 右
            result.append(root.val) # 后序

        traversal(root)
        return result